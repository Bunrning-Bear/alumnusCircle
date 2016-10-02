#!usr/bin/env python
# coding=utf-8
# message.py
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
        """
            my_circle_list: to get all of message updated in mysql.
        """
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
        logging.info(" result of get message %s"%result)
        self.return_to_client(code,message,result)
        self.finish()

class CheckMessageHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(CheckMessageHandler, self).__init__(*argc, **argkw)
        self.requestName='check_message'

    @request.authenticated('check_message')
    @tornado.gen.coroutine  
    def post(self):
        """
            needn't post parameter.
        """
        uid = self.get_secure_cookie('uid')
        self.message.return_message_check(uid)
        code = 0
        message = "successfully clear message."
        code = self.return_code_process(code)
        self.return_to_client(code,message)

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
        Args:
            count   integer     否   30              返回结果的数量，默认为30
            type    string      否   received        received我收到的,
                                                     sent我发出的,
                                                     默认为received
            page    integer     否   1               页码，默认为1
        
        Returns:
            "response": {
                "count": 30,
                "total": 6,
                "page": 1,
                "results": [        
                           {
                                "status": 0,
                                "feed": {
                                    "status": 0,
                                    "creator": {# 不要
                                        "icon_url": "http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg",
                                        "medal_ids": "empty",
                                        "id": "57d2c60fd36ef3ede3236ebb",
                                        "source_uid": "15888888888",
                                        "name": "15888888888大神"
                                    },
                                    "image_urls": [#不要 
                                        "http://tupian.qqjay.com/tou3/2016/0605/9848ad4d58f2cf2ac07a2645d66e20e6.jpg",
                                        "http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg"
                                    ],

                                    "content": "这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!",
                                    "create_time": "2016-09-10 00:33:17",
                                    "readable_create_time": "00:33",＃　不要
                                    "id": "57d2e44dd36ef3fbfcb032e4"
                                },
                                "stats": {＃不要
                                    "liked": 0
                                },
                                "floor": 7, #不要
                                "creator": {
                                    "icon_url": "http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg",
                                    "medal_ids": "empty",
                                    "id": "57d2f9dab9a9963aecd1af26",
                                    "source_uid": "15644444444",
                                    "name": "15644444444你哪呢"
                                },
                                "reply_user": "empty",　＃不要
                                "content": "[很长]我评论了这条动态! 我评论了这条动态!我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! 我评论了这条动态! ",　
                                "source": "社区", #不要
                                "create_time": "2016-09-10 02:49:01",　
                                "image_urls": "empty",
                                "reply_comment": "empty",
                                "id": "57d3041dd36ef3fc508b167f",
                                "readable_create_time": "02:49"
                            }
        """

        info_json = self.get_argument('info_json')
        Data = json.loads(info_json)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self.get_redis_dict_access_token(uid)
        count,message,umengData =yield self.Umeng_asyn_request(access_token,Data)
        # umengData = json.loads(umengData)
        # logging.info("data in comment list \n %s"%umengData['results'])
        for dictUnit in umengData['results']:
            del dictUnit['status']
            del dictUnit['feed']['status']
            del dictUnit['feed']['creator']
            del dictUnit['feed']['image_urls']
            del dictUnit['feed']['readable_create_time']
            del dictUnit['feed']['id']            
            del dictUnit['feed']['create_time']            
            del dictUnit['stats']
            del dictUnit['floor']     
            del dictUnit['reply_user']  
            del dictUnit['source']   
            del dictUnit['reply_comment']
            del dictUnit['readable_create_time']  
            del dictUnit['image_urls']
        code = self.return_code_process(count)
        self.return_to_client(code,message,umengData)
        self.finish()