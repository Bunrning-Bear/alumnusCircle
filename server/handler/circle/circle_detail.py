#!/usr/bin/env python
# coding=utf-8
# circle_detal.py

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

from handler import user
from handler import base
from handler import request
import modules.review_deal
import modules.circle
from common.lib.prpcrypt import prpcrypt,set_encrypt
from common.lib.to_list import custom_list_to_list
from handler.request import RequestHandler

"""get a special infomation of a circle.
"""
class DetailCircleHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(DetailCircleHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic'
        self.methodUsed = 'GET'    
        self.requestName ='topicdetail'

    @request.authenticated('topicdetail')        
    @tornado.web.asynchronous
    @tornado.gen.coroutine        
    def post(self):
        """
            info_json:
                topic_id:
        """
        Data = self.get_argument('info_json')
        Data = json.loads(Data)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self._public_access
        code,message,Data = yield self.public_Umeng_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()

"""
    get feed list belong to a special circle.
"""
class CircleFeedListHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(CircleFeedListHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/topic_timeline'
        self.methodUsed = 'GET'    
        self.requestName ='circle_feed'

    @request.authenticated('circle_feed')        
    @tornado.web.asynchronous
    @tornado.gen.coroutine      
    def post(self):
        """
            info_json:
                count:   integer     否   30  返回结果的数量，默认为30
                topic_id:    string  是   无   话题id
                max_id  string  否   无   返回id小于max_id的数据
                page    integer     否   1   页码，默认为1
                since_id    string  否   无   返回id大于since_id的数据
                order   integer     否   无   0(默认): 按最新发布时间排序,
                                            1：按最新评论时间排序，
                                            2：按最新赞时间排序，
                                            3：按最新被转发时间排序，
                                            4：按评论或赞或转发最新时间排序
        """
        Data = self.get_argument('info_json')
        Data = json.loads(Data)
        uid = self.get_secure_cookie('uid')
        code = 0
        code,message,Data = yield self.public_Umeng_request(Data)
        self.return_to_client(code,message,Data)
        self.finish()

class CircleMemberHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(CircleMemberHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/fans'
        self.methodUsed = 'GET'    
        self.requestName ='circle_member'

    @request.authenticated('circle_member')        
    @tornado.web.asynchronous
    @tornado.gen.coroutine      
    def post(self):
        """
            count   integer     否   30  返回结果的数量，默认为30
            max_id  string  否   无   返回id小于max_id的数据
            page    integer     否   1   页码，默认为1
            topic_id    string  是   无   话题ID
        """
        Data = self.get_argument('info_json')
        Data = json.loads(Data)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self.get_redis_dict_access_token(uid)
        logging.info("circle member of access_token : %s"%access_token)
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()