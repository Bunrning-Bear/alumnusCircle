#!/usr/bin/env python
# coding=utf-8
# contact.py
#Author ChenXionghui
"""
contact :
    1. get all of user in elasticsearch.
    2. filter by all of user.
    3. keyword search.
    4. user detail
"""
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
import modules.review_deal
import modules.circle
from common.lib.prpcrypt import prpcrypt,set_encrypt
from common.lib.to_list import custom_list_to_list
from request import RequestHandler
from base import BaseHandler

"""
    base handler of cantact part.
"""
class ContactHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(ContactHandler, self).__init__(*argc, **argkw)
        # self._elastic_user_module 
"""
    Get All of User in Our App. and you can filter it through pass some parameter.
"""
class UserFilterHandler(ContactHandler):
    def __init__(self, *argc, **argkw):
        super(UserFilterHandler, self).__init__(*argc, **argkw)     
        self.requestName = 'user_filter'

    @request.authenticated('user_filter')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
        filter_admission_year_min: 入学年份的最小值
        filter_admission_year_max：入学年份的最大值
        filter_major_list ：专业筛选列表
        filter_city_list：居住城市筛选列表
        all_match ：0 模糊搜索；1 筛选搜索；2获取全部用户
        query     ：筛选语句
        page：分页的页码
        size：每页显示的数据数
        """
        filter_admission_year_min=int(self.get_argument("filter_admission_year_min"))
        filter_admission_year_max=int(self.get_argument("filter_admission_year_max"))
        filter_major_list = json.loads(self.get_argument("filter_major_list"))
        filter_city_list = json.loads(self.get_argument("filter_city_list"))
        all_match = self.get_argument("all_match")
        query = self.get_argument("query")
        page = int(self.get_argument("page"))
        size = int(self.get_argument("size"))
        logging.info("filter_major_list : %s type is %s"%(filter_major_list,type(filter_major_list)))
        Data = self._elastic_user_module.keyword_search(
            all_match,query,filter_admission_year_min,filter_admission_year_max,
            filter_major_list,filter_city_list,page,size)
        code = 5000
        message = "success"
        self.return_to_client(code,message,Data)
        self.finish()

"""
    get a special user's detail information by uid [mysql]
"""
class UserDetailHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(UserDetailHandler, self).__init__(*argc, **argkw)
        self.requestName = 'user_detail'
        self.methodUsed= 'GET'
        self.url = '/0/user'

    @request.authenticated('user_detail')
    @tornado.gen.coroutine
    def post(self):
        user_id = self.get_argument('uid')
        umeng_id =self.user_module.get_umeng_id_from_uid(user_id)
        uid = self.get_secure_cookie('uid')
        access_token = self.user_module.get_access_token_from_uid(uid)['access_token']
        Data = {'uid':umeng_id}
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        code = 0
        message = "get detail user successfully"
        self.return_to_client(code,message,Data)
        self.finish()

