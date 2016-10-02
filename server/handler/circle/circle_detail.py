#!/usr/bin/env python
# coding=utf-8
# circle_detal.py
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
        access_token = self.get_redis_dict_access_token(uid)
        count,message,umengData =yield self.Umeng_asyn_request(access_token,Data)   
        self.return_to_client(code,message,umengData)
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
        "response": {
            "count": 10,
            "total": 2,
            "page": 1, 
            "results": [
                {
                    "liked": false,
                    "seq": 3638198,# 不要
                    "creator": {
                        "icon_url": "http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg",
                        "medal_ids": "empty",# 不要
                        "id": "57d2c60fd36ef3ede3236ebb",
                        "source_uid": "15888888888", # 不要
                        "name": "15888888888大神"
                    },
                    "topics": [ #不要
                        {
                            "stats": "empty",
                            "description": "大神再此，带你装逼，带你飞",
                            "icon_url": "http://img1.imgtn.bdimg.com/it/u=1372134302,958716461&fm=206&gp=0.jpg",
                            "image_urls": "empty",
                            "custom": {
                                "virtual_cid": "57d2dd11b9a9967859f14f8",
                                "creator_uid": "30",
                                "creator_name": "大神"
                            },
                            "id": "57d2dd11d36ef3fc508aee94",
                            "name": "带你装逼，带你飞 二号"
                        }
                    ],
                    "tag": 0,　＃ 不要
                    "readable_create_time": "00:33", # 不要
                    "id": "57d2e44dd36ef3fbfcb032e4",
                    "stats": {
                        "liked": 0,
                        "forwards": 0,
                        "comments": 6
                    },
                    "title": "circle feed list !",
                    "origin_feed": "empty", # 不要
                    "custom": "",#不要
                    "content": "这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!",
                    "source": "社区",　＃　不要
                    "location": "empty",＃不要
                    "media_type": 0,#不要
                    "type": 0,＃不要
                    "status": 0,#不要
                    "is_topic_top": "empty",＃不要
                    "image_urls": [
                        "http://tupian.qqjay.com/tou3/2016/0605/9848ad4d58f2cf2ac07a2645d66e20e6.jpg",
                        "http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg"
                    ],
                    "is_top": 0,#不要
                    "topic_tag": "",＃不要
                    "related_users": "empty",#不要
                    "has_collected": false,＃　不要
                    "create_time": "2016-09-10 00:33:17",
                    "parent_feed_id": "",＃不要
                    "is_recommended": true,＃　不要
                    "share_link": "http://wsq.umeng.com/feeds/57d2e44dd36ef3fbfcb032e4/"　＃不要
                },
        """
        Data = self.get_argument('info_json')
        Data = json.loads(Data)
        uid = self.get_secure_cookie('uid')
        code = 0
        access_token = self.get_redis_dict_access_token(uid)
        count,message,umengData =yield self.Umeng_asyn_request(access_token,Data)
        for dictUnit in umengData['results']:
            del dictUnit['seq']
            del dictUnit['creator']['medal_ids']
            del dictUnit['creator']['source_uid']       
            del dictUnit['topics']
            del dictUnit['tag']
            del dictUnit['readable_create_time']     
            del dictUnit['origin_feed']     
            del dictUnit['custom']
            del dictUnit['source']
            del dictUnit['location']
            del dictUnit['media_type']
            del dictUnit['type']
            del dictUnit['status']

        self.return_to_client(code,message,umengData)
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