#!/usr/bin/env python
# coding=utf-8
# base.py

"""
Processed logic:

when:
openApp-->search['uid']
try to login and has check his password sucessful--->get uid
--->todo:set it to cookie?
other request, get cookie['uid'] before.


--->has get uid:
    --->empty?
        --->empty--->get_current_user('uid')[which f @tornado.web.authenticated]
        |   --->redirect Handler.[implement: http://www.cnblogs.com/apexchu/p/4239844.html]                          
        |   --->tell client,your cookie is outdate, your identifier is unlogin[visitor] now.  

----------------those will been implement by get_current_user() and redirect function---------------                   
-------------------those are needn't when login and register------------------------------------
        --->not empty:
            ---> User_dict['uid'] exist? 
                ---> no[0] --->login, and set User_dict['uid](_xsrf,access_token).-->sucessful login. 
                                                                                     [todo]: relogin in request. openApp-->password has been changed.
                |
                ---> yes:
                    --->_xsrf == _xsrf in User_dict['uid'](xsrf,access_token)?                                     
                    |
                    --->equal[1] ---> start request logic. openApp auto login. send login request several time, just ignore.
                    |
                    --->different[2]---> ignore request logic or openApp, account been login by other user. when login, just change value of _xsrf.
---------------those will been implement by user_dict_check function, return 0,1,2------------------------
"""
"""
base.py define BaseHandler, which is parent class all of other classes.
"""
import os
import ConfigParser
import functools
import logging
import json
import modules.user
import modules.message
import modules.ec_user
import urllib
import tornado.web
import tornado.gen
import tornado.httpclient

from modules.uploadimg import Aliyun
from common.lib.prpcrypt import set_encrypt

from common.variables import AP,CODE_DICT



class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self._db = self.application.db
        self._redis_dict = self.application._redis_dict
        # load all of variable needed into BaseHandler.
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'/common/conf.ini'))
        self._aes_key = config.get('app','secret')
        self._appkey = config.get('app','appkey')
        self._prefix = config.get('url','prefix')
        self._public_access = config.get('app','public_access')
        self._virtual_access = config.get('app','virtual_access')
        # load all of module operate into BaseHandler.
        self._user_module = modules.user.UserInfoModule(self._db)
        self._user_list_module = modules.user.UserListModule(self._db)
        self._user_detail_module = modules.user.UserDetailModule(self._db)
        self._user_message_module = modules.message.UserMessageModule(self._db)
        self._code_dict =CODE_DICT
        self._elastic_user_module = modules.ec_user.ElasticUserModule(self.application.es)
        logging.info("request is : %s \n \n"%self.request)
        args = self.request.arguments
        logging.info("request arguments: %s"%args)

    @property
    def elastic_user_module(self):
        return self._elastic_user_module
    
    @property
    def user_module(self):
        return self._user_module

    @property    
    def user_list_module(self):
        return self._user_list_module

    @property
    def user_detail_module(self):
        return self._user_detail_module

    @property
    def user_message_module(self):
        return self._user_message_module
    
    def get_current_user(self):
        """
        If this function return None 0 or [], function which has decorator
        "@tornado.web.authenticated" will redirect to the Handler login_url
        has define.
        """
        return self.get_secure_cookie("uid")
    # [todo]2016.8.4 user_dict should been store in redis   
    def redis_dict_check(self,uid,_xsrf):
        """
        Check the status of user_dict

        Args:
        uid: [string] the key of user_dict.
        _xsrf: [string] the _xsrf value pass from client.

        Returns:
        0: user_dict has no key of uid
        1: user_dict[uid] is not equal to _xsrf.
        2: user_dict[uid] is not equal to _xsrf.

        """
        if not self._redis_dict.hexists("user:" + str(uid),"_xsrf"):
            return 0
        elif self._redis_dict.hget("user:" + str(uid),"_xsrf") != _xsrf:
            return 1
        else:
            return 2

    def set_redis_dict(self,uid,_xsrf,access_token,last_update_time,adlevel=0):
        """Set User_dict when login.
        """
        dic = {
        "_xsrf":_xsrf,
        "last_update_time":last_update_time,
        "access_token":access_token,
        "adlevel":adlevel}
        
        self._redis_dict.hmset("user:" + str(uid),dic)
        # self.message.init_message(uid)
        
    def get_redis_dict(self,uid):
        return self._redis_dict.hvals("user:"+str(uid))

    def get_redis_dict_access_token(self,uid):
        return self._redis_dict.hget("user:"+str(uid),"access_token")

    def delete_redis_dict(self,uid):
        self._redis_dict.hdel("user:" + str(uid),"_xsrf")

    def get_user_last_update_time(self,uid):
        return self._redis_dict.hget('user:'+str(uid), "last_update_time")
    # [todo]:2016.8.26 restructure the logic of return code.
    def return_code_process(self,code):
        """Return status code to client after get a code from handler.

        Args:
        handler:[string] must be a name of handler such as "reigster" or "login"
        code: [int] status code in a handler.

        Returns:
        [string] global status code.
        """
        return self._code_dict[self.requestName] + code

    def return_to_client(self,code,message, Data = {}):
        """
        This method is to return status code and message to client.
        
        Args:
            code[string]: a global status code.
            It will be created by function return_code_process or Umeng's 'err_code'(look for detail at UmengApi)
            message[string]: the meaning to status code.
            Data[dictory]:this is a optional parameter the data should response to client
        Returns:
            not return, just send {'code':code,'message':message} json string to client.
        """

        update_Data = self.get_user_update()
        Data={'update':update_Data,'response':Data}
        temp = str(json.dumps(Data))# json
        # logging.info(" data : %s"%Data)
        temp = temp.replace("null","\"empty\"")
        json_after_replace = json.loads(temp)#dict
        # logging.info("response code%s message%s  data is : %s"%(code,message,json_after_replace))
        self.change_custom_string_to_json(json_after_replace)# change custom type

        if Data == {}:
            resultJson = json.dumps({'code':code - 1,'message':message,'Data':{}})
        else:
            resultJson = json.dumps({'code':code,'message':message,'Data':json_after_replace})
        logging.info('json returned to client is :%s'%resultJson)        
        self.write(resultJson) 
#        self.finish()

    def get_user_update(self):
        return {}

    def change_custom_string_to_json(self, dic):
        if isinstance(dic,dict):
            for key,value in dic.items():
                # print "in dictory : ",key, value
#               if value == [] or value == {}:
                    # change all of empty list and dicotry to "empty"
#                    dic[key] = str("empty")
                if type(value) == bool:
                    dic[key] = str(value)
                elif key == 'custom' and value !='' and dic[key] !={}:
                    # change custom string into json style data.
                    # print "in custom:%s type is : %s"%(value,type(value))
                    try:
                        dic[key] = json.loads(value)
                    except Exception, e:
                        try:
                            dic[key]  = eval(value)
                        except Exception, e:
                            dic[key] = value
                elif key == 'icon_url' and isinstance(value,dict) and dic[key] != {}:
                    # delete 360.720 origin.
                    dic[key] = value['origin']
                
                    dic[key] = Aliyun().parseUrlByFakeKey(dic[key])
                elif key == 'image_urls' and isinstance(value,list) and dic[key] != []:
                    count = 0
                    while count < len(value):
                        dic[key][count] = value[count]['origin']
                        dic[key][count] = Aliyun().parseUrlByFakeKey(dic[key][count])                        
                        count += 1
                if isinstance(value,dict):
                    self.change_custom_string_to_json(value)
                elif isinstance(value,list):
                    # print " out of list ", value
                    for list_value in value:
                        # print "in list : "+str(list_value)
                        self.change_custom_string_to_json(list_value)

