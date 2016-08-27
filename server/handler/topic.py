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
from common.lib.prpcrypt import prpcrypt,set_encrypt
from request import RequestHandler
from base import BaseHandler

class CeateTopicHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(CeateTopicHandler, self).__init__(*argc, **argkw)
        self.url = '/0/topic/create'
        self.methodUsed = 'POST'    
        self.requestName ='topic'

    @request.authenticated('topic')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        count = 0
        name = "custom topic"
        customJson = json.dumps({"creator":"fange","admin":"xionghui"})
        Data = {"name":str(name),"custom":str(customJson)}
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self.get_user_dict(uid)[1]
        logging.info("access %s and Data %s:"%(access_token,Data))
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)
        count = count + 1
        self.finish()

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