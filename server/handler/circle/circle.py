#!/usr/bin/env python
# coding=utf-8
# topic.py
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
import pdb
from handler import user
from handler import base
from handler import request
import modules.review_deal
import modules.circle
from common.lib.prpcrypt import prpcrypt,set_encrypt
from common.lib.to_list import custom_list_to_list
from handler.request import RequestHandler



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
        logging.info("umeng uid is : %s"%umeng_uid)
        code,message,Data = yield self.Umeng_asyn_request(access_token,Data)

        raise tornado.gen.Return((code,message,Data))

    @request.authenticated('focus_on_circle')        
    @tornado.gen.coroutine      
    def focus_on_circle(self,uid,topic_id):
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
    def post(self):
        result_data = []
        my_filter_circle = self.get_argument('my_filter_circle')
        my_filter_circle_list = custom_list_to_list(my_filter_circle)
        logging.info(" before mapping  my admin circle list : %s"%my_filter_circle_list)
        my_filter_circle_list = map(self.circle_module.get_circle_umeng_cid,my_filter_circle_list)
        uid = self.get_secure_cookie('uid')
        logging.info("my admin circle list %s"%my_filter_circle_list)
        code,message,Data = yield self.get_user_topic(uid)
        logging.info("get user topic :%s"%Data)
        total = 0
        for value in my_filter_circle_list:
            count = 0
            while count < len(Data['results']):
                logging.info(" value is %s , circle is %s"%(value,Data['results'][count]['id'] ))
                if Data['results'][count]['id'] == value:
                    logging.info(" count is : %s  data resuls count is :%s"%(count,Data['results']))
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
    def post(self):
        """
            circle_name:
            circle_icon_url:
            creator_uid:
            creator_name
            circle_type_id:
            circle_type_name:
            reason_message:
            description
        """

        circle_name = self.get_argument(self.message_review_module._circle_name)
        circle_icon_url = self.get_argument(self.message_review_module._circle_icon_url)

        creator_name = self.get_argument(self.message_review_module._creator_name)
        creator_uid = self.get_argument(self.message_review_module._creator_uid)
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


class ReviewListHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(ReviewListHandler, self).__init__(*argc, **argkw)

    def get(self):
        # [todo] data check
        result = int(self.get_argument("result"))
        max_id = self.get_argument("max_id")
        limit_num = self.get_argument("limit_num")
        if result == 0 or result == 1:
            Data = self.message_review_module.get_review_list(result,max_id,limit_num)
            logging.info("review list data is : %s"%Data)
            if result == 0:
                self.render('to_review.html',resultdata=Data)
            else:
                self.render('has_review.html',resultdata=Data)
        else:
            Data = []
            self.return_to_client(1,"fail",Data)
    


class ReviewResultHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(ReviewResultHandler, self).__init__(*argc, **argkw)
        self.requestName= "review_topic"

    @request.authenticated('review_topic')
    @tornado.gen.coroutine
    def post(self):
        """
            result: must be 1 or 2.
                1: agree
                2: reject
            review_id : the entities id of the manual review information
        """
        result = int(self.get_argument("result"))
        review_id = self.get_argument("review_id")
        count = 1
        if result > 2 or result <=0:
            code = self.return_code_process(count)
            self.return_to_client(0,"fail")
        else:
            if result == 1:
                # agree create new circle.
                count,message,Data = yield self.__createUmengTopic(review_id,virtual=True)
                if count != 0:
                    # create virtual circle failed.
                    code = count
                    self.return_to_client(code,message,Data)
                    self.finish()
                    return
                else:                  
                    # create virtual circle success, now create real circle.  
                    virtual_cid = Data['id']
                    count,message,Data = yield self.__createUmengTopic(review_id,virtual=False,virtual_cid=virtual_cid)
                    if count != 0:
                        code = count
                        self.return_to_client(code,message,Data)
                        self.finish()
                        return
                    else:                       
                        real_cid = Data['id']
                        cid = self.circle_module.set_circle_info(real_cid,virtual_cid,Data['icon_url'])
                        #cid = self.circle_module.set_circle_info(real_cid,virtual_cid,Data['type_id'],Data['icon_url'])
                        logging.info("cid is: %s"%cid)
                        # create success message to member of circle.
                        mid = self.message.create_message(
                            self.message.TYPE['create circle success'],
                            circle_name=Data['name'],circle_url=Data['icon_url'],circle_id=real_cid)
                        mc_id = self.message_circle_module.set_circle_info(cid,real_cid)
                        self.message.add_new_message_queue_to_all(cid)
                        # add my_create_circle
                        self.user_detail_module.add_create_circle_list(cid,Data['creator_uid'])
                        # [todo]: add follow funcion
                        count,message,umengdata =yield self.focus_on_circle(Data['creator_uid'],real_cid)
                        if count != 0 :
                            code = count
                            self.return_to_client(code,message,Data)
                            self.finish()
                            return                            
                        self.return_to_client(0,message,Data)
            else:
                mid = self.message.create_message(
                    self.message.TYPE['create circle fail'],
                    circle_name=Data['name'],circle_url=Data['icon_url'])
            # update review.
            logging.info("result is %s review_id is %s"%(result,review_id))
            self.message_review_module.update_review_result(result,review_id)                
            # send result message to creator
            self.message.deal_message_to_one(mid,Data['creator_uid'])
            self.return_to_client(1,"success",Data)
        self.finish()

    @tornado.gen.coroutine
    def __createUmengTopic(self,review_id,virtual,virtual_cid =''):
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
        Data = self.message_review_module.get_review_by_id(review_id)
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
            Data['icon_url'] = icon_url
            Data['creator_uid']=creator_uid
        raise tornado.gen.Return((code,message,Data))

class ApplyTopicHanlder(TopicHandler):
    pass
    
"""
    After admin deal the apply message, execute user's apply result.
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
    def post(self):
        """
            result: 0 or 1 receive result. 0 reject ,1 agree.
            apply_user_id: apply user id.
            apply_user_name: needn't when reject.
            circle_id:
            circle_url:
            circle_name:
            review_id:
        """
        result = int(self.get_argument("result"))
        apply_user_id = self.get_argument("apply_user_id")
        circle_id = self.get_argument("circle_id")
        circle_url = self.get_argument("circle_url")
        circle_name = self.get_argument("circle_name")
        # todo : check if the message has been review by other user.
        if result == 0:
            # create message to applyer, tell he review result
            mid2 = self.message.create_message(type_id=self.message.TYPE['appply circle result'],
                circle_name=circle_name,circle_id=circle_id,circle_url=circle_url,result=result)
            # send message to apply user.
            self.message.deal_message_to_one(mid1,apply_user_id)
            code = self.return_code_process(0)
            message = "reject successfully!"
            Data = {}
        else:
            # agree, follow.
            username = self.get_argument('apply_user_name')
            topic_id = self.circle_module.get_circle_umeng_cid(circle_id)
            # get apply user access token.
            access_token = self.user_module.get_access_token_from_uid(apply_user_id)['access_token']
            logging.info("topic id is : %s access_token is : %s"%(topic_id,access_token))
            # follow to umeng.
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
                # create message to applyer, tell he review result
                mid2 = self.message.create_message(type_id=self.message.TYPE['apply circle result'],
                    circle_name=circle_name,circle_id=circle_id,circle_url=circle_url,result=result)
                # send message to apply user.
                self.message.deal_message_to_one(mid1,apply_user_id)
        self.return_to_client(code,message,Data)
        self.finish()

class AdminSetHandler(TopicHandler):
    pass

"""
    [needn't this version] edit circle information 
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

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        Data = self.get_argument("info_json")
        Data = json.loads(Data)
        code = 0
        access_token = self._public_access
        code,message,Data = yield self.public_Umeng_request(Data)
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
    def post(self):
        Data = self.get_argument('info_json')
        Data = json.loads(Data)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self._virtual_access
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()