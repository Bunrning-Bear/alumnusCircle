#!/usr/bin/env python
# coding=utf-8
#user_list.py
"""
This file define classes about reponse some list.
example:
    get follows list
    get fans list
    get comment list
    get like list
    get my favorites list
    get my feed list
"""
import json
import tornado.web
import tornado.gen
import request
import base
from request import RequestHandler
"""
[needn't]
Get all of user I follows.
user can not get others followslist, although Umeng api can do so.
"""
class FollowsListHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(FollowsListHandler, self).__init__(*argc, **argkw)
        self.url = '/0/user/follows'
        self.methodUsed = 'GET'
        self.requestName = 'followsList'   

    @request.authenticated('followsList')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
        Requet from client:
            info_json:
                page:
                uid:
                count:
                max_id:
        """
        # page = self.get_argument('page')
        # user_id = self.get_argument('uid')
        # count = self.get_argument('count')
        # Data = {'page':page,'count':self.count,"uid":user_id}
        """
            GET value page from client:
            page[integer]:[must] represent the page will return the next request.
        """
        info_json = self.get_argument('info_json')
        Data = json.loads(info_json)
        user_id = Data['uid']
        umeng_id = self.user_module.get_umeng_id_from_uid(user_id)
        Data['uid']=umeng_id
        uid = self.get_secure_cookie('uid')
        access_token = self.get_redis_dict_access_token(uid)
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)    
        #code,message = self.umeng_Api(self.url,self._public_access,Data,0,self.methodUsed)
        self.return_to_client(code,message,Data)    
        self.finish() 

#[todo]:count should be resquest by client?

class FansListHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(FollowsListHandler, self).__init__(*argc, **argkw)
        self.url = '/0/user/fans'
        self.methodUsed = 'GET'
        self.count =10
        self.requestName = 'fansList'   
    
    @request.authenticated('fansList')
    @tornado.web.asynchronous
    @tornado.gen.coroutine    
    def post(self):
        page = self.get_argument('page')
        uid = self.get_argument('uid')
        Data = {'page':page,'count':self.count,"uid":uid}
        """
            GET value page from client:
            page[integer]:[must] represent the page will return the next request.
        """
        uid = self.get_secure_cookie('uid')
        access_token = self.get_user_dict(uid)[1]
        code,message =yield self.Umeng_asyn_request(access_token,Data)    
        #code,message = self.umeng_Api(self.url,self._public_access,Data,0,self.methodUsed)
        self.return_to_client(code,message)    


"""
Get my favorites list include all of feed it favorite

"""
class FavouriteslistHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(FavouriteslistHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/favourites'
        self.methodUsed = 'GET'
        self.count =10
        self.requestName = 'favourites'

    @request.authenticated('favourites')
    @tornado.gen.coroutine    
    def get(self):
        page = self.get_argument('page')
        Data = {'page':page,'count':self.count}
        """
            GET value page from client:
            page[integer]:[must] represent the page will return the next request.
       """
        uid = self.get_secure_cookie('uid')
        access_token = self.get_user_dict(uid)[1]
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)    
        #code,message = self.umeng_Api(self.url,self._public_access,Data,0,self.methodUsed)
        self.return_to_client(code,message,Data)    
        self.finish()

