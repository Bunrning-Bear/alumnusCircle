#!usr/bin/env python
# coding=utf-8
# message.py
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

"""
    Get my new message.
"""
class GetMessageHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(GetMessageHandler, self).__init__(*argc, **argkw)
        self.requestName='sendmessage'

    @request.authenticated('sendmessage')
    @tornado.gen.coroutine  
    def post(self):
        uid = self.get_secure_cookie('uid')
        my_circle_list = self.get_argument('my_circle_list')
        last_update_time = self.get_user_last_update_time(uid)
        logging.info("last_update_time in post :%s"%last_update_time)
        result = self.message.check_and_get_message(uid,my_circle_list,last_update_time)
        if result == {}:
            code = 1
            message = "your message list has not been updated yet"
        else:
            code = 0
            message = "get message successfully"
        code = self.return_code_process(code)
        self.return_to_client(code,message,result)
        self.finish()

"""
    Get my comment list by timeline
"""
class GetMyCommentHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(GetMyCommentHandler, self).__init__(*argc, **argkw)
        self.requestName='get_comment_list' 
        self.url = '/0/my/comments'
        self.methodUsed = 'GET' 

    @request.authenticated('get_comment_list')
    @tornado.gen.coroutine  
    def post(self):
        """
        count   integer     否   30              返回结果的数量，默认为30
        type    string      否   received        received我收到的,
                                                 sent我发出的,
                                                 默认为received
        page    integer     否   1               页码，默认为1
        """
        info_json = self.get_argument('info_json')
        Data = json.loads(info_json)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self.get_redis_dict_access_token(uid)
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()