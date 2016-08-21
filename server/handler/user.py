#!/usr/bin/env python
# coding=utf-8
# user.py
"""
user.py define classes about login, logout, register.
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
import tornado.gen

import user
import base
import request
from common.lib.prpcrypt import prpcrypt,set_encrypt
from request import RequestHandler
from base import BaseHandler

"""
 user handler :include register login and logout
"""

class UserHandler(RequestHandler):
    _regex_dict = {}
    def __init__(self, *argc, **argkw):
        super(UserHandler, self).__init__(*argc, **argkw)
        # ref: http://blog.jobbole.com/96052/
        # phone number begin with 13 or 14 or 15 or 17 or 18, 
        # length allowed is: 11.
        self._regex_dict[self.user_module._user_phone] = ur"^13[\d]{9}$|^14[5,7]{1}\d{8}$|^15[^4]{1}\d{8}$|^17[0,6,7,8]{1}\d{8}$|^18[\d]{9}$\Z"
        # begin with letter, length between 6 and 18, all allowed char are letter, number and underline.
        # length allowed is: 6 to 18
        self._regex_dict[self._user_module._user_password] = ur"^[a-zA-Z]\w{5,64}$\Z"
        # username should been decode with 'utf8',all allowed are chinese char, letter, number and underline.
        # length allowed is: 6 to 16
        self._regex_dict[self.user_list_module._name] = ur"^[\u4e00-\u9fa5\w\s]{1,20}$"
        # the smallest qq id is 10000
        # wechat id can be letter, number and underline
        # admission year : 1000~ 2999
        self._regex_dict[self.user_list_module._admission_year] = ur"^[1-2][0-9]{3}$\Z"
        # faculty id 0~99
        self._regex_dict[self.user_list_module._faculty_id] = ur"^[0-9]{1,2}$\Z"
        # major id 0~99
        self._regex_dict[self.user_list_module._major_id] = ur"^[0-9]{1,2}$\Z"
        # gender
        self._regex_dict[self.user_list_module._gender] = ur"^[0-1]$\Z"
        # job
        self._regex_dict[self.user_list_module._job] = ur"^[\u4e00-\u9fa5\w]{2,20}$"
        # city
        self._regex_dict[self.user_list_module._city] = ur"^[0-9]{3,3}$\Z"
        # company 
        self._regex_dict[self._user_detail_module._company]=ur"^[\u4e00-\u9fa5\w\s]{2,25}$"

    def _check_unit(self,check_type,string):
        """Check if the user information input is valid.

        Args:
            check_type: [string] can be self.user_module._user_phone self._user_module._user_password or something else which is the json's key(which is client request).
            string: [string] the value of the key type. 

        Returns:
            False: did not matched.
            True: matched.
        """
        
        regex = self._regex_dict[check_type]
        if check_type == self.user_list_module._name:
            logging.info("username %s"%string)
            string = string.decode('utf-8')
        result = False
        if re.match(regex,string):
            result = True
        """
                if check_type ==self._user_module._user_qq or check_type ==self._user_module._user_wechat:
                    if string =='':
                        result = True
        """
        return result
    
    def _check(self,Data):
        """
        Check every element of Data, find the invalid element and 
        return the code, message, and code count.
        
        Args:
            Data:[json] Input Data which is json type.
            The element of Data can be self._user_module._user_name,self._user_module._user_password or others, look for _regex_dict
        
        Returns:
            code number: represent by count value.
            message: explain the meaning of code.
        """
        count = 0
        
        message = ''
        # check all of key-value is valid through UserModule._check function
        for key, value in Data.items():
            # logging.info("key:%s value:%s"%(str(key),str(value)))
            equal = self._check_unit(str(key),str(value))
            message = key
            if not equal:
                break              
            count = count + 1

        if count == len(Data):
            message = "all data input is valid, this message will not appear in normal"
        else: 
            message = "%s format error"%message
        return count, message


class RegisterHandler(UserHandler):
    def __get_cryptedData(self,Data):
        """Encrypted data from user infromation to Umeng.
        
        Args:
        Data:[json] this is the request from client.

        Returns:
        encrypted data.
        """
        source = "self_account"
        UmengData = {
        "user_info":{"name":str(Data[self._user_module._user_phone])},
        "source_uid":str(Data[self.user_module._user_phone]),
        "source":source} 
        # logging.info("umengdata: %s"%UmengData)
        cryptedData = set_encrypt(self._aes_key,UmengData)
        return cryptedData

    @tornado.web.asynchronous       
    @tornado.gen.coroutine
    def post(self):
        """
        Request from client:
            POST['info_json'][string]:
                "user_phone"
                "user_passwd"
                "name"
                "admission_year"
                "faculty_id"
                "gender"
                "major_id"
                "job"
                "city"
                "company"
        """
        jsonData = self.get_argument('info_json')
        Data = json.loads(jsonData)
        count,message = self._check(Data)
        code = self.return_code_process('register',count)
        if count == len(Data):
            hasRegister = self.user_module.find_user_phone(Data[self.user_module._user_phone])
            if hasRegister:
                code =code + 1 
                message = "User phone:%s has been register "%Data[self.user_module._user_phone]
            else:
                code = code + 1
                message = "register successful!"
                cryptedData = self.__get_cryptedData(Data)
                url = self._prefix+"/0/get_access_token?ak=" + self._appkey
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                body = urllib.urlencode({"encrypted_data":cryptedData})
                client = tornado.httpclient.HTTPClient()
                request = tornado.httpclient.HTTPRequest(
                    url=url,
                    method="POST",
                    headers=headers,
                    body=body
                )
                response = yield tornado.gen.Task(client.fetch,request)
                body =  json.loads(response.body)
                if "err_code" in body:
                    code = body['err_code']
                    message = body['err_msg']
                else:
                    access_token = body['access_token']
                    #[test]:just set a random stu id.
                    stu_id = random.randint(10000000,99999999)
                    user_id = self.user_module.set_info_to_user(
                        access_token,
                        # Data[self._user_module._user_name], [todo]: I think user name is needn't in mysql.
                        Data[self._user_module._user_password],
                        Data[self.user_module._user_phone],
                        stu_id)
                    logging.info("after register code is %s message is %s"%(code,message))
                    # use update pai to set user's message.
                    # [todo]: should not write data to mysql before get successful information in umeng data.
                    self.url = '/0/user/update'
                    self.methodUsed = 'PUT'
                    self.requestName = 'update_user_info'
                    admission_year = Data[self.user_list_module._admission_year]
                    faculty_id = Data[self.user_list_module._faculty_id]
                    major_id = Data[self.user_list_module._major_id]
                    job = Data[self.user_list_module._job]
                    city = Data[self.user_list_module._city]
                    company = Data[self.user_detail_module._company]
                    real_name = Data[self._user_list_module._name]
                    phone = Data[self._user_module._user_phone]
                    custom = {
                    # "uni_id":1,# todo: uni_id == 1 ,prestent the SEU.
                    "admission_year":admission_year,
                    "faculty_id":faculty_id,
                    "major_id":major_id,
                    "job":job,
                    "uid":user_id,
                    "publicity_level":0,
                    "city":city,
                    "real_name":real_name,
                    }
                    custom = json.dumps(custom)                    
                    gender = Data[self._user_list_module._gender]

                    icon_url = "default"
                    #[todo]I think user id is useless, right?
                    Data = {
                    "gender":gender,
                    "name":phone,
                    # "icon_url":icon_url,[you should change your url at another api]
                    "custom":custom
                    # "uid":uid
                    }
                    code,message,Data = yield self.Umeng_asyn_request(access_token,Data)
                    logging.info('after umeng request, code is %s message is %s'%(code,message))
                    if code == 0:
                        # set umeng data success.
                        # [todo]xionghui:2016.8.21 all of thos operate should be atomic operation
                        self.user_list_module.set_info_to_user(
                            user_id,admission_year,faculty_id,major_id,real_name,gender,job,icon_url,city)
                        self.user_detail_module.set_info_to_user(
                            user_id,admission_year,faculty_id,major_id,real_name,gender,job,icon_url,city,company)
                        message = "register successfully!"
                    # logging.info('user_id :%s'%user_id)
        # encode message and code to json, send to client.
        self.return_to_client(code,message)
        self.finish()

#[todo]:2016.8.21 add auto login logic
class LoginHandler(UserHandler):
    def post(self):
        """
        Request from client:
            POST['info_json'][string]:
                "user_passwd"
                "user_phone"         
        """
        jsonData = self.get_argument('info_json')
        _xsrf = self.get_argument('_xsrf')
        Data = json.loads(jsonData)        
        # check the validity of data request.
        count,message = self._check(Data)
        code = self.return_code_process('login',count)
        if count == len(Data):
            phone = Data[self.user_module._user_phone]
            entity = self.user_module.get_info_from_phone(phone)
            if entity == []:
                code = code + 1
                message = "the phone has not been register now."
                self.return_to_client(code,message)
                self.finish()
            else:
                if Data[self._user_module._user_password] != entity[0][self._user_module._user_password]:
                    message = "your input a wrong password"
                else:
                    uid = str(entity[0][self.user_module._uid]) 
                    code = code + 1
                    result = self.user_dict_check(str(uid), str(_xsrf))
                    # logging.info("login uid is %s _xsrf is %s result is %s"%(uid,_xsrf,result))
                    if result == 0:
                        message = "login successfully!"
                    elif result == 1:
                        code = code + 1
                        message = "login successfully! another user been logout!"
                    else:
                        code = code + 2
                        message = "you have login! needn't do it again!"
                    access_token = entity[0]['access_token']
                    uid = entity[0]['uid']
                    Data = self.user_detail_module.get_info_from_uid(uid)
                    # logging.info("data in mysql ac_user_detail_info is :%s"%Data)
                    # set cookie and dict
                    self.set_user_dict(str(uid),_xsrf,access_token)
                    self.set_secure_cookie('uid',str(uid))
                    self.return_to_client(code,message,Data[0])
                    self.finish()


class LogoutHandler(UserHandler):
    def __init__(self, *argc, **argkw):
        super(LogoutHandler, self).__init__(*argc, **argkw)
        self.requestName = 'logout'

    @request.authenticated(str('logout'))
    def post(self):
        """
        Request just nothing.
        """
        uid = self.get_secure_cookie('uid')
        _xsrf = self.get_argument('_xsrf')
        count = 0
        if not uid:
            message ="invalid logout, uid (in cookie) is not valid"
        else:
            count = count + 1
            result = self.user_dict_check(str(uid),str(_xsrf))
            if result == 0:
                message = "the account has been logout"
            elif result == 1:
                count = count + 1
                message = "_xsrf is wrong, can not logout"
            elif result == 2:
                count = count + 2
                message = "logout successfully!"
                self.delete_user_dict(str(uid))
                self.clear_cookie('uid')
        self.return_to_client(count,message)
        self.finish()

# [todo]: 2016.8.21 ,we just save all of list include contact_list job_list as json string.
# it will be low-efficient when update, but it is convenient.
# consider that update is not a high frequent operate
# so we just save data as a json string rather than some entities for each contact record and job record.  
class UpdataInfoHandler(UserHandler):
    def __init__(self, *argc, **argkw):
        super(UpdataInfoHandler, self).__init__(*argc, **argkw)
        self.requestName = 'update_user_info'

    @request.authenticated(str('update_user_info'))
    @tornado.web.asynchronous
    @tornado.gen.coroutine    
    def post(self):
        """
        POST from client:
        POST['list_info_has_update']:bool: if list info has been update, set value true[1].
        info_json:
            'custom':json： if list_info_has_update, client dumps custom field to this parameter.
                "admission_year":admission_year,
                "faculty_id":faculty_id,
                "major_id":major_id,
                "job":job,
                "uid":user_id,
                "publicity_level":0,
                "city":city,
                "real_name":real_name,
            'telephone': this parameter must be stored in client.
        [those field is used in Umeng update].
        POST['icon_url']:
        POST['publicity_level']:
        POST['city']:
        POST['job']:
        POST['public_contact_list']
        POST['protect_contact_list']
        POST['job_list']
        POST['job_list_level']
        POST['company']
        POST['company_publicity_level ']
        POST['instoduction']
        """
        self.url = '/0/user/update'
        self.methodUsed = 'PUT'
        code = 0 
        uid = self.get_secure_cookie('uid')
        update_list = self.get_argument('list_info_has_update')
        logging.info("update_list%s"%update_list)
        if update_list:
            DataJson = self.get_argument('info_json')
            Data = json.loads(DataJson)            
            access_token = self.get_user_dict(uid)[1]
            code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
            logging.info("in update_list to umeng")
        if code != 0:
            # request Umeng error!
            self.return_to_client(code,message)
            self.finish()
        else:
            icon_url = self.get_optional_argument('icon_url')
            publicity_level = self.get_optional_argument('publicity_level')
            city = self.get_optional_argument('city')
            job = self.get_optional_argument('job')
            public_contact_list = self.get_optional_argument('public_contact_list')
            protect_contact_list = self.get_optional_argument('protect_contact_list')
            job_list = self.get_optional_argument('job_list')
            job_list_level = self.get_optional_argument('job_list_level')
            company = self.get_optional_argument('company')
            company_publicity_level = self.get_optional_argument('company_publicity_level')
            instoduction = self.get_optional_argument('instoduction')
        if update_list:
            