#!/usr/bin/env python
# coding=utf-8
"""
this file define all of handlers from user to user.
include:
    follow and unfollow
"""
import json

import tornado.web
import tornado.gen

import base
import request
from request import RequestHandler

"""
Complete follow and unfollow operate
    
"""
class FollowHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(FollowHandler, self).__init__(*argc, **argkw)
        self.url = '/0/user/'
        self.methodUsed = 'POST'
        self.requestName = 'follow'

    @request.authenticated('follow')
    @tornado.web.asynchronous
    @tornado.gen.coroutine    
    def post(self):
        """
        Request from client:
            POST['target']:can be follow or unfollow,to define the url.
            POST['info_json']:      
                "target_uid":[string][must] the user you want to follow
        """
        target = self.get_argument('target')
        uid = self.get_secure_cookie('uid')
        self.url = self.url + target
        user_id = self.get_argument('uid')
        umeng_id = self.user_module.get_umeng_id_from_uid(user_id)
        Data = {'target_uid':umeng_id}
        access_token = self.get_redis_dict_access_token(uid)
        count,message,Data =yield self.Umeng_asyn_request(access_token,Data) 
        code = self.return_code_process(count)      
        self.return_to_client(code,message,Data)

"""
[needn't]
search a user by part of "username"

"""
class SearchUserHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(SearchUserHandler, self).__init__(*argc, **argkw)
        self.url = '/0/user/search/'
        self.methodUsed = 'GET'
        self.requestName = 'searchuser'
        self.count = 10

    @request.authenticated('searchuser')
    @tornado.web.asynchronous
    @tornado.gen.coroutine    
    def get(self):
        """
        Request from client:
            GET['page']:[integer][must]represent the page will return the next request.
            GET['q']:[string][must]this is a part of or whole username to search.
        """
        uid = self.get_secure_cookie('uid')
        page = self.get_argument('page')
        q = self.get_argument('q')
        Data = {"count":self.count,"page":page,"q":q}
        access_token = self.get_redis_dict_access_token(uid)
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)       
        self.return_to_client(code,message)
        self.finish()

