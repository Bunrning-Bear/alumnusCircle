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

import user
import base
import request
import modules.message_deal
from common.lib.prpcrypt import prpcrypt,set_encrypt
from request import RequestHandler
from base import BaseHandler


class TopicHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(TopicHandler, self).__init__(*argc, **argkw)
        self._message_review_module = modules.message_deal.ReviewCircleModule(self._db)

"""user send a create circle request, store it in mysql.
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
            circle_type_id:
            reason_message:
        """
        circle_name = self.get_argument(self._message_review_module._circle_name)
        circle_icon_url = self.get_argument(self._message_review_module._circle_icon_url)
        creator_uid = self.get_argument(self._message_review_module._creator_uid)
        # creator_uid
        circle_type_id = self.get_argument(self._message_review_module._circle_type_id)
        reason_message = self.get_argument(self._message_review_module._reason_message)
        description = self.get_argument(self._message_review_module._description)
        review_id = self._message_review_module.set_new_review_message(
            circle_name,circle_icon_url,creator_uid,circle_type_id,reason_message,description)
        # todo : add error and type check.
        Data = {"review_id":review_id}
        self.return_to_client(0,"success",Data)
        self.finish()


class ReviewListHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(ReviewListHandler, self).__init__(*argc, **argkw)   

    def post(self):
        # [todo] data check
        result = int(self.get_argument("result"))
        since_id = self.get_argument("since_id")
        limit_num = self.get_argument("limit_num")
        if result == 0 or result == 1:
            Data = self._message_review_module.get_review_list(result,since_id,limit_num)
            self.return_to_client(0,"success",Data)
        else:
            Data = []
            self.return_to_client(1,"fail",Data)
        self.finish()


class ReviewResultHandler(TopicHandler):
    def __init__(self, *argc, **argkw):
        super(ReviewResultHandler, self).__init__(*argc, **argkw)
        self.requestName= "review_topic"

    @request.authenticated('review_topic')
    @tornado.gen.coroutine
    def post(self):
        """
            result: must be 1 or 2
        """
        result = int(self.get_argument("result"))
        review_id = self.get_argument("review_id")
        count = 1
        if result > 2 or result <=0:
            code = self.return_code_process(count)
            self.return_to_client(0,"fail",Data)
        else:
            Data = self._message_review_module.update_review_result(result,review_id)
            if result == 1:
                code,message,Data = yield self.createUmengTopic(review_id)
                self.return_to_client(code,message,Data)
        self.finish()

    @tornado.gen.coroutine
    def createUmengTopic(self,review_id):
        self.url = '/0/topic/create'
        self.methodUsed='POST'
        Data = self._message_review_module.get_review_by_id(review_id)

        name = Data[self._message_review_module._circle_name]
        # description = Data['description']
        icon_url = Data[self._message_review_module._circle_icon_url]
        description = Data[self._message_review_module._description]
        creator_uid = Data[self._message_review_module._creator_uid]
        custom = {"creator_uid":creator_uid}
        custom = json.dumps(custom)
        # todo : this access_token must get by a real admin user.
        Data = {
        "name":name,
        "icon_url":icon_url,
        "description":description,
        "custom":custom
        }
        access_token = self._virtual_access
        code,message,Data = yield self.Umeng_asyn_request(access_token,Data)
        raise tornado.gen.Return((code,message,Data))


class DetailTopicHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(DetailTopicHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic'
        self.methodUsed = 'GET'    
        self.requestName ='topicdetail'


    @tornado.web.asynchronous
    @tornado.gen.coroutine        
    def post(self):
        Data = self.get_argument('info_json')
        Data = json.loads(Data)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self._public_access
        code,message,Data = yield self.public_Umeng_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()


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
        code,message,Data = yield self.public_Umeng_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()


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