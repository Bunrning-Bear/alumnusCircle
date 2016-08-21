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
import tornado.web
import tornado.gen
import request
import base
from request import RequestHandler
"""
Get all of user I follows.
user can not get others followslist, although Umeng api can do so.
"""
class FollowsListHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(FollowsListHandler, self).__init__(*argc, **argkw)
        self.url = '/0/user/follows'
        self.methodUsed = 'GET'
        self.count =10
        self.requestName = 'followsList'   

    @request.authenticated('followsList')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        """
        Requet from client:
            GET['page']:
            GET['uid']: this is umeng uid store in user's cookie.
        """
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
    @tornado.web.asynchronous
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
        code,message =yield self.Umeng_asyn_request(access_token,Data)    
        #code,message = self.umeng_Api(self.url,self._public_access,Data,0,self.methodUsed)
        self.return_to_client(code,message)    

