#!/usr/bin/env python
# coding=utf-8
# topic.py
#Author ChenXionghui
import json
import re
import ConfigParser
import struct
import base64
import urllib
import pdb
import logging
import random

import tornado.httpclient
import tornado.web
from modules.uploadimg import Aliyun

from handler import user
from handler import base
from handler import request
import modules.review_deal
import modules.circle
from common.lib.prpcrypt import prpcrypt,set_encrypt
from common.lib.to_list import custom_list_to_list
from handler.request import RequestHandler


"""This is base handler for all of handler about circle.

This handler has those functions:
1. define some related modules;
2. define some common functions, most of about umneg api.
"""
class TopicHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(TopicHandler, self).__init__(*argc, **argkw)
        self._message_review_module = modules.review_deal.ReviewCircleModule(self._db)
        self._circle_module = modules.circle.CircleModule(self._db)
        self._message_circle_module= modules.message.MessageCircleModule(self._db)

    @property
    def message_review_module(self):
        return self._message_review_module

    @property
    def circle_module(self):
        return self._circle_module

    @property
    def message_circle_module(self):
        return self._message_circle_module

    @request.authenticated('user_topic')        
    @tornado.gen.coroutine       
    def get_user_topic(self,uid):
        """Get all of cirlce user has followed, include join, admin and create.

        Args:
            uid: the circle want to return.

        Returns:
        """
        self.requestName= "user_topic"
        self.url = '/0/topic/user/topics'
        self.methodUsed = 'GET'    
        access_token = self.get_redis_dict_access_token(uid)
        umeng_uid = self.user_module.get_umeng_id_from_uid(uid)
        logging.info("uid is %s"%uid)
        Data = {
        "count":300,
        "page":1,
        "uid":umeng_uid
        }
        # logging.info("umeng uid is : %s"%umeng_uid)
        code,message,Data = yield self.Umeng_asyn_request(access_token,Data)
        raise tornado.gen.Return((code,message,Data))

    @request.authenticated('focus_on_circle')        
    @tornado.gen.coroutine      
    def focus_on_circle(self,uid,topic_id):
        """To follow a circle for a special user.
        In our app, "follow" function will not been operated by client directly.
        all of "follow" operate need to "apply" and "review"
        
        Args:
            uid: the user id who want to follow a circle.
            topic_id: target circle id
        
        Returns:

        """
        self.requestName= "receive_apply"
        self.url = '/0/topic/focus'
        self.methodUsed = 'POST'    
        #[todo]: delete ['access_token']
        access_token = self.user_module.get_access_token_from_uid(uid)['access_token']
        # umeng_uid = self.user_module.get_umeng_id_from_uid(uid)
        # logging.info("uid is %s"%uid)
        Data = {
        "topic_id":topic_id,
        }
        code,message,Data = yield self.Umeng_asyn_request(access_token,Data)

        raise tornado.gen.Return((code,message,Data))
        

""" Get all of circle I have followed.
"""
class GetMyCircleHandler(TopicHandler):
    def __init__(self, *argc, **argkw):    
        super(GetMyCircleHandler, self).__init__(*argc, **argkw)
        self.requestName = 'get_all_topic'

    @request.authenticated('get_all_topic')
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        uid = self.get_secure_cookie('uid')
        code,message,Data = yield self.get_user_topic(uid)
        self.return_to_client(code,message,Data)
        self.finish()


"""Get my admin circle and my create circle.
"""
class GetMyfilterCircleHander(TopicHandler):
    def __init__(self, *argc, **argkw):    
        super(GetMyfilterCircleHander, self).__init__(*argc, **argkw)
        self.requestName = 'get_my_filter_circle'

    @request.authenticated('get_my_filter_circle')
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        """Get my admin circle and my create circle.

        Implement though 'get_my_filter_circle' parameter.
        Client pass 'my_admin_circle' or 'my_create_cirlce'.
        We get all of user's circles and filter by this parameter and return to client.

        Post Args:
            'my_filter_circle':client should pass 'my_admin_circle' or 'my_create_cirlce'.

        Returns:

        """
        result_data = []
        my_filter_circle = self.get_argument('my_filter_circle')
        my_filter_circle_list = custom_list_to_list(my_filter_circle)
        # logging.info(" before mapping  my admin circle list : %s"%my_filter_circle_list)
        my_filter_circle_list = map(self.circle_module.get_circle_umeng_cid,my_filter_circle_list)
        uid = self.get_secure_cookie('uid')
        # logging.info("my admin circle list %s"%my_filter_circle_list)
        code,message,Data = yield self.get_user_topic(uid)
        # logging.info("get user topic :%s"%Data)
        total = 0
        for value in my_filter_circle_list:
            count = 0
            while count < len(Data['results']):
                # logging.info(" value is %s , circle is %s"%(value,Data['results'][count]['id'] ))
                if Data['results'][count]['id'] == value:
                    # logging.info(" count is : %s  data resuls count is :%s"%(count,Data['results']))
                    result_data.append(Data['results'][count])
                    total += 1
                count += 1
        Data['results']= result_data
        Data['total'] = total
        self.return_to_client(code,message,Data)
        self.finish()

"""User send a create circle request, store it in mysql.

"""
class CeateTopicHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(CeateTopicHandler, self).__init__(*argc, **argkw)
        self.requestName = 'create_topic'
        
    @request.authenticated('create_topic')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        """User send a create circle request, store it in mysql. app amin will review it later.

        Args:
            circle_name:
            circle_icon_url:
            creator_uid:
            creator_name
            circle_type_id:
            circle_type_name:
            reason_message: the reason why user want to create this circle.
            description:circle description

        Returns:

        """

        circle_name = self.get_argument(self.message_review_module._circle_name)
        circle_icon_url = self.get_argument(self.message_review_module._circle_icon_url)

        creator_name = self.get_argument(self.message_review_module._creator_name)
        creator_uid = self.get_secure_cookie('uid')
        # creator_uid
        circle_type_name = self.get_argument(self.message_review_module._circle_type_name)
       # circle_type_id = self.get_argument(self.message_review_module._circle_type_id)

        reason_message = self.get_argument(self.message_review_module._reason_message)
        description = self.get_argument(self.message_review_module._description)

        review_id = self.message_review_module.set_new_review_message(
            circle_name,circle_icon_url,creator_uid,circle_type_name,reason_message,description,creator_name)
        # todo : add error and type check.
        Data = {"review_id":review_id}
        code = self.return_code_process(0)
        self.return_to_client(code,"success send create circle message.",Data)
        self.finish()

"""Get to-review list or has-review list.
"""
class ReviewListHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(ReviewListHandler, self).__init__(*argc, **argkw)


    def get(self):
        """Get to-review list or has-review list for admin user.

        Args:
            result: 0 stand for to-erview list. 1 stand for has-review list.
            max_id: pass the largest number this time, pass 0 for the first time.
            limit_num: to get the max num for a page.

        Returns:
        
        return example:
            [
                {
                    "result": 0,
                    "circle_icon_url": "http: //www.seu.edu.cn/4838461475374051.16.jpg",
                    "circle_name": "\\u521b\\u4e1a\\u534f\\u4f1a\\u603b\\u90e8",
                    "circle_type_name": "\\u793e\\u56e2\\u5708",
                    "review_id": 42,
                    "creator_name": "\\u9648\\u5c0f\\u718a",
                    "creator_uid": "127",
                    "reason_message": "\\u6211\\u662f\\u521b\\u534f2016\\u5e74\\u4f1a\\u957f\\uff0c\\u7533\\u8bf7\\u521b\\u5efa\\u5e76\\u7ba1\\u7406\\u8fd9\\u4e2a\\u5708\\u5b50",
                    "description": "\\u521b\\u4e1a\\u534f\\u4f1a\\u6210\\u7acb\\u81ea2000\\u5e74\\uff0c\\u6c47\\u805a\\u4e86\\u4e1c\\u5927\\u6700\\u6fc0\\u60c5\\u4e0e\\u70ed\\u8840\\u7684\\u4e00\\u6279\\u4eba\\u3002\\u6211\\u8fd9\\u4e2a\\u7fa4\\u7ed9\\u521b\\u534f\\u5185\\u90e8\\u4eba\\u4f7f\\u7528\\uff0c\\u65b9\\u4fbf\\u5927\\u5bb6\\u4ea4\\u6d41\\u548c\\u8d44\\u6e90\\u5bf9\\u63a5"
                },
                {
                    "result": 0,
                    "circle_icon_url": "http: //www.seu.edu.cn/192781473786574.34.jpg",
                    "circle_name": "\\u4eba\\u5de5\\u667a\\u80fd\\u5708",
                    "circle_type_name": "\\u5174\\u8da3\\u5708",
                    "review_id": 39,
                    "creator_name": "\\u9648\\u5c0f\\u718a",
                    "creator_uid": "127",
                    "reason_message": "\\u4e3a\\u4eba\\u5de5\\u667a\\u80fd\\u5708\\u63d0\\u4f9b\\u4ea4\\u4e92\\u5e73\\u53f0",
                    "description": "\\u667a\\u80fd\\u65f6\\u4ee3\\uff0c\\u4ea4\\u6362\\u60f3\\u6cd5\\uff0c\\u4ea4\\u6362\\u601d\\u60f3\\uff0c\\u4f60\\u6211\\u90fd\\u4f1a\\u662f\\u4e00\\u4e2a\\u8fd9\\u4e2a\\u667a\\u80fd\\u65f6\\u4ee3\\u7684\\u667a\\u8005\\u3002"
                }
            ]
        """
        def __url_filter(unit):
            logging.info("unit creator is %s"%(unit['circle_icon_url']))
            unit['circle_icon_url'] = Aliyun().parseUrlByFakeKey(unit['circle_icon_url'])
            return unit
        # [todo] data check
        result = int(self.get_argument("result"))
        max_id = self.get_argument("max_id")
        limit_num = self.get_argument("limit_num")
        
        if result == 0 or result == 1:
            Data = self.message_review_module.get_review_list(result,max_id,limit_num)
            # url filter:
            Data = filter(__url_filter,Data)
            logging.info("review list data is : %s"%Data)
            if result == 0:
                self.render('to_review.html',resultdata=Data)
            else:
                self.render('has_review.html',resultdata=Data)
        else:
            Data = []
            self.return_to_client(1,"fail",Data)
    
"""App admin user review a special create-circle apply.
"""
class ReviewResultHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(ReviewResultHandler, self).__init__(*argc, **argkw)
        self.requestName= "review_topic"

    @request.authenticated('review_topic')
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        """App admin user review a special create-circle apply.
        
        If reject, just send result message to creator.
        If agree:
            * send result message to creator;
            * create virtual circle for this new create circle.[virtual circle is used to update 'contact me' feed]
            * create circle in umeng and store circle data in mysql;
            * follow this new creatre circle for user;
            * update user data in mysql (create_circle_list)

        Args:
            result: must be 1 or 2. 
                1: agree
                2: reject
            review_id : the entities id of the manual review information
        
        Returns:

        """
        result = int(self.get_argument("result"))
        review_id = self.get_argument("review_id")
        reviewData = self.message_review_module.get_review_by_id(review_id)
        count = 1
        if result>2 or result<=0:
            code = self.return_code_process(count)
            self.return_to_client(0,"fail")
        else:
            if result == 1:
                # agree create new circle.
                count,message,umengData = yield self.__createUmengTopic(reviewData,virtual=True)
                if count != 0:
                    # create virtual circle failed.
                    code = count
                    self.return_to_client(code,message)
                    self.finish()
                    return
                else:                  
                    # create virtual circle success, now create real circle.  
                    virtual_cid = umengData['id']
                    count,message,umengData = yield self.__createUmengTopic(reviewData,virtual=False,virtual_cid=virtual_cid)
                    if count != 0:
                        code = count
                        self.return_to_client(code,message)
                        self.finish()
                        return
                    else:                       
                        real_cid = umengData['id']
                        cid = self.circle_module.set_circle_info(real_cid,virtual_cid,reviewData[self.message_review_module._circle_icon_url])
                        #cid = self.circle_module.set_circle_info(real_cid,virtual_cid,Data['type_id'],Data['icon_url'])
                        logging.info("cid is: %s"%cid)
                        # create success message to member of circle.
                        mid = self.message.create_message(
                            self.message.TYPE['create circle success'],
                            circle_name=reviewData[self.message_review_module._circle_name],circle_url=reviewData[self.message_review_module._circle_icon_url],circle_id=real_cid)
                        mc_id = self.message_circle_module.set_circle_info(cid,real_cid)
                        self.message.add_new_message_queue_to_all(cid)
                        # add my_create_circle
                        self.user_detail_module.add_create_circle_list(cid,reviewData[self.message_review_module._creator_uid])
                        # 】follow circle
                        count,message,umengdata =yield self.focus_on_circle(reviewData[self.message_review_module._creator_uid],real_cid)
                        if count != 0 :
                            code = count
                            self.return_to_client(code,message)
                            self.finish()
                            return                        
            else:
                mid = self.message.create_message(
                    self.message.TYPE['create circle fail'],
                    circle_name=reviewData[self.message_review_module._circle_name],circle_url=reviewData[self.message_review_module._circle_icon_url])
            # update review.
            logging.info("result is %s review_id is %s"%(result,review_id))
            self.message_review_module.update_review_result(result,review_id)                
            # send result message to creator
            self.message.deal_message_to_one(mid,reviewData[self.message_review_module._creator_uid])
            self.return_to_client(1,"success",reviewData)
        self.finish()

    @tornado.gen.coroutine
    def __createUmengTopic(self,Data,virtual,virtual_cid =''):
        """Create topic in Umeng database.
        In this app, we define "virtual circle" to store those feed upload by user out of circle.
        
        data structure in umeng:
         {
                    "stats": {
                        "fans": 1,
                        "feeds": 0
                    },
                    "description": "thecirclewillbebeautiful!",
                    "tags": [],
                    "icon_url": {
                        "80": "empty",
                        "160": "empty",
                        "origin": "empty"
                    },
                    "image_urls": [],
                    "custom": {
                        "virtual_cid": "57c69cbab9a9965edeffa3e7",
                        "creator_uid": "123"
                    },
                    "secret": false,
                    "create_time": "2016-08-3117: 00: 43",
                    "has_followed": true,
                    "id": "57c69cbbb9a99622684b2d23",
                    "name": "newcircle397"
                },

        Args:
            review_id[int]: the entities in ac_manual_review_table. to get the apply information.
            virtual[bool]: if true, we will create a virtual circle, else we will create a real circle.
                we should create virtual circle before create realcircle.
            virtual_cid[int]:virtual circle umeng id, you should add this parameter if you are creating a real circle.

        Returns:
            code,message the same to Umeng_asyn_request.
            Data add a field call "type_id". store the circle type id in umeng. 
        """
        self.url = '/0/topic/create'
        self.methodUsed='POST'
        logging.info("data in creator umeng topic is .%s"%Data)
        #　type_id = Data[self.message_review_module._circle_type_id]
        result = Data[self.message_review_module._result]
       #  pdb.set_trace() 
        if result != 0:
            code = self.return_code_process(1)
            message = 'this message has been review'
            Data = {}
        else:
            if virtual:
                name = str("virtual_") + str(Data[self.message_review_module._circle_name])
            else:
                name = str(Data[self.message_review_module._circle_name]) 
            # description = Data['description']
            icon_url = Data[self.message_review_module._circle_icon_url]
            description = Data[self.message_review_module._description]
            creator_uid = Data[self.message_review_module._creator_uid]
            creator_name = Data[self.message_review_module._creator_name]
            # todo : add admin user property
            if not virtual:
                custom = {"creator_uid":creator_uid,"creator_name":creator_name,"virtual_cid":virtual_cid}
            else:
                custom = {"creator_uid":creator_uid,"creator_name":creator_name}
            custom = json.dumps(custom)
            # todo : this access_token must get by a real admin user.
            Data = {
            "name":name,
            "icon_url":str(icon_url),
            #[test todo]: when we get a real url, this should be use.
            "description":description,
            "custom":custom
            }
            access_token = self._virtual_access
            logging.info("topic data is %s"%Data)
            code,message,Data = yield self.Umeng_asyn_request(access_token,Data)
            # Data['type_id'] = type_id
        raise tornado.gen.Return((code,message,Data))


"""
    After circle admin deal a apply message, execute apply result for circle admin user.
"""
class ReceiveApplyReviewHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(ReceiveApplyReviewHandler, self).__init__(*argc, **argkw)
        self.requestName= "receive_apply"
        self.url = '/0/topic/focus'
        self.methodUsed = 'POST'    

    @request.authenticated('receive_apply')        
    @tornado.web.asynchronous
    @tornado.gen.coroutine   
    @request.throwBaseException
    def post(self):
        """After circle admin deal a apply message, execute apply result for circle admin user.
        If result == 0 :[means reject]
            just send message to applicant;
        If result == 1 :[means agree]
            * follow this circle for the apply in umeng
            * update user data info in mysql (my_circle_list)
            * send result message to applicant;
            * send new member message to all of member in the circle.
        
        Post Args:    
            result: 0 or 1 receive result. 0 reject ,1 agree.
            apply_user_id: apply user id.
            apply_user_name: needn't when reject.
            circle_id:
            circle_name:
            review_id:

        Returns:
        """
        result = int(self.get_argument("result"))
        apply_user_id = self.get_argument("apply_user_id")
        circle_id = self.get_argument("circle_id")
        logging.info("circle id after change is %s"%circle_id)
        circle_url = self.circle_module.get_icon_url_from_cid(circle_id)
        circle_name = self.get_argument("circle_name")
        # todo : check if the message has been review by other user.
        if result == 0:
            # create message to applicant, tell he review result
            mid2 = self.message.create_message(type_id=self.message.TYPE['appply circle result'],
                circle_name=circle_name,circle_id=circle_id,circle_url=circle_url,result=result)
            # send message to apply user.
            self.message.deal_message_to_one(mid2,apply_user_id)
            code = self.return_code_process(0)
            message = "reject successfully!"
            Data = {}
        else:
            # agree, follow.
            username = self.get_argument('apply_user_name')
            # get apply user access token.
            access_token = self.user_module.get_access_token_from_uid(apply_user_id)['access_token']
            # logging.info("topic id is : %s access_token is : %s"%(topic_id,access_token))
            # follow to umeng.
            topic_id = self.circle_module.get_circle_umeng_cid(circle_id)
            Data = {
                "topic_id":topic_id
            }
            code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
            if code == 0 :
                # update user info data.
                Data = {}
                Data['update']= self.user_detail_module.update_my_circle_list(circle_id,apply_user_id) 
                # create message to all of member in the circle, to tell them new member.      
                mid1 = self.message.create_message(type_id=self.message.TYPE['new member'],
                    circle_name=circle_name,circle_id=circle_id,circle_url=circle_url,uid=apply_user_id,username=username)
                # set message to circle queue.
                self.message.deal_message_to_all(mid1,circle_id)
                # create message to applicant, tell he review result
                mid2 = self.message.create_message(type_id=self.message.TYPE['apply circle result'],
                    circle_name=circle_name,circle_id=circle_id,circle_url=circle_url,result=result)
                # send message to apply user.
                self.message.deal_message_to_one(mid2,apply_user_id)
        self.return_to_client(code,message,Data)
        self.finish()

class AdminSetHandler(TopicHandler):
    pass


"""
    [needn't this version] edit circle information 
    update: icon_url,name,description.
"""
class EditTopicHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(EditTopicHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/edit'
        self.methodUsed = 'POST'    
        self.requestName ='topicedit'

    @request.authenticated('topicedit')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        Data = self.get_argument('info_json')
        Data = json.loads(Data)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self._virtual_access
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()


class GetTopicTypeHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(GetTopicTypeHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/category/topics'
        self.methodUsed = 'GET'    
        self.requestName ='topictype'

    @request.authenticated('topictype')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        Data = self.get_argument("info_json")
        uid = self.get_secure_cookie('uid')
        access_token = self.get_redis_dict_access_token(uid)
        Data = json.loads(Data)
        code = 0
        code,message,Data = yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()

"""
    [needn't] needn't this version.
    search circle by circle name.
"""
class SearchTopicHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(SearchTopicHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/search'
        self.methodUsed = 'GET'    
        self.requestName ='searchtopic'

    @request.authenticated('searchtopic')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        Data = self.get_argument('info_json')
        Data = json.loads(Data)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self._virtual_access
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()