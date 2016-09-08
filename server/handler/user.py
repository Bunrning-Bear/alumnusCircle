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
import chardet

import tornado.httpclient
import tornado.web
import tornado.gen
import pdb
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
        # faculty  0~99
        self._regex_dict[self.user_list_module._faculty] = ur"^[\u4e00-\u9fa5\w]{2,20}$"
        # major id 0~99
        self._regex_dict[self.user_list_module._major] = ur"^[\u4e00-\u9fa5\w]{2,20}$"
        # gender
        self._regex_dict[self.user_list_module._gender] = ur"^[0-1]$\Z"
        # job
        self._regex_dict[self.user_list_module._job] = ur"^[\u4e00-\u9fa5\w]{2,20}$"
        # city
        self._regex_dict[self.user_list_module._city] = ur"^[\u4e00-\u9fa5\w]{1,20}$"
        # state
        self._regex_dict[self.user_list_module._state] = ur"^[\u4e00-\u9fa5\w]{2,20}$"# ur"^[\x{4e00}-\x{9fa5}\w]{2,20}$"    
        # country
        self._regex_dict[self.user_list_module._country] =ur"^[\u4e00-\u9fa5\w]{2,20}$"            
        # company 
        self._regex_dict[self._user_detail_module._company]=ur"^[\u4e00-\u9fa5\w\s]{2,25}$"
        # icon_url is a url or a string "default"
        self._regex_dict[self._user_list_module._icon_url] = ur"^((https|http)?:\/\/)[^\s]+|default$\Z"
        

    def data_decode(self,to_decode_data):
        # pdb.set_trace()
        logging.info("data: %s "%type(to_decode_data))
        for key,value in to_decode_data.items():
            if isinstance(value,str):
                coding_type = chardet.detect(value)['encoding']
                if coding_type !='unicode':
                    to_decode_data[key] = value.decode('utf-8')

    def _check_unit(self,check_type,string):
        """Check if the user information input is valid.

        Args:
            check_type: [string] can be self.user_module._user_phone self._user_module._user_password or something else which is the json's key(which is client request).
            string: [string] the value of the key type. 

        Returns:
            False: did not matched.
            True: matched.
        """
#        if check_type == self._user_module._user_password: 
        #pdb.set_trace()
        regex = self._regex_dict[check_type]
        # print "check unit :%s"%chardet.detect(string)['encoding']
        #print "coding type %s"%coding_type
        if isinstance(string,str):
            coding_type = chardet.detect(string)['encoding']
            if coding_type != 'unicode':
                string = string.decode('utf-8')
        result = False
        # pdb.set_trace()
        try:
            
            if re.match(regex,string):
                result = True
            else:
                print "failed string :%s"%string
                print "failed type : %s" %type(string) 
                print "failed regex : %s"%regex
        except Exception, e:
            print "error string :%s"%string
            print "error type : %s" %type(string) 
            print "error regex : %s"%regex
            print e
            raise
        finally:
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
        count = 1
        
        message = ''
        # check all of key-value is valid through UserModule._check function
        # print "data in check %s"%Data
        for key, value in Data.items():
            # logging.info("key:%s value:%s"%(str(key),str(value)))
            equal = self._check_unit(str(key),str(value))
            message = key
            if not equal:
                break              
            count = count + 1
        if (count - 1) == len(Data):
            message = "all data input is valid, this message will not appear in normal"
            count = 0
        else: 
            message = "%s format error"%message
        return count, message


class CheckTelephoneHandler(UserHandler):
    def __init__(self, *argc, **argkw):
        super(CheckTelephoneHandler, self).__init__(*argc, **argkw)
        self.requestName ='check_phone'

    def post(self):
        count = 0
        phone = self.get_argument(self.user_module._user_phone)
        if self._check_unit(self.user_module._user_phone,phone):
            hasRegister = self.user_module.find_user_phone(phone)
            if hasRegister:
                count =1 
                message = "User phone:%s has been register "%phone
            else:
                count = 2
                message = "this phone can be used."
        else:
            count = 3
            message = "telephone format error!"
        code = self.return_code_process(count)
        self.return_to_client(code,message)
        self.finish()

class RegisterHandler(UserHandler):
    def __init__(self, *argc, **argkw):
        super(RegisterHandler, self).__init__(*argc, **argkw)
        self.requestName = 'register'
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

        code = 0
        jsonData = self.get_argument('info_json')
        Data = json.loads(jsonData)
        #print "data before %s"%Data
        #self.data_decode(Data)
        #print "data decode : %s"%Data
        count,message = self._check(Data)
        if count != 0:
            code = self.return_code_process(count)
            self.return_to_client(code,message)
            self.finish()
        else:
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
                logging.info("after register code is %s message is %s"%(count,message))
                # use update pai to set user's message.
                # [todo]: should not write data to mysql before get successful information in umeng data.
                self.url = '/0/user/update'
                self.methodUsed = 'PUT'
                self.requestName = 'update_user_info'
                admission_year = Data[self.user_list_module._admission_year]
                faculty = Data[self.user_list_module._faculty]
                major = Data[self.user_list_module._major]
                job = Data[self.user_list_module._job]
                city = Data[self.user_list_module._city]
                state = Data[self.user_list_module._state]
                country = Data[self.user_list_module._country]
                company = Data[self.user_detail_module._company]
                real_name = Data[self._user_list_module._name]
                phone = Data[self._user_module._user_phone]
                custom = {
                # "uni_id":1,# todo: uni_id == 1 ,prestent the SEU.
                "admission_year":admission_year,
                "faculty":faculty,
                "major":major,
                "job":job,
                "uid":user_id,
                "publicity_level":0,
                "city":city,
                "state":state,
                "country":country,
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
                if code == 0:
                    # set umeng data success.
                    # [todo]xionghui:2016.8.21 all of thos operate should be atomic operation
                    umeng_id = Data['id']
                    logging.info("data after umeng  of register is : %s"%Data['id'])
                    logging.info("data user id is : %s"%user_id)
                    code = self.return_code_process(count)
                    self.user_list_module.set_info_to_user(
                        user_id,admission_year,faculty,major,real_name,gender,job,icon_url,city,state,country)
                    self.user_detail_module.set_info_to_user(
                        user_id,admission_year,faculty,major,real_name,gender,job,icon_url,city,state,country,company)
                    self.user_message_module.set_user_to_message(user_id)
                    self.user_module.update_umeng_id(umeng_id,user_id)
                    res = self.elastic_user_module.createInfo(user_id,faculty,major,real_name,country,state,city,admission_year,icon_url,job,company)
                    logging.info("elastic_user_module : %s"%res)
                    message = "register successfully!"

                    # logging.info('user_id :%s'%user_id)
        # encode message and code to json, send to client.
        self.return_to_client(code,message)
        self.finish()

#[todo]:2016.8.21 add auto login logic
class LoginHandler(UserHandler):
    def __init__(self, *argc, **argkw):
        super(LoginHandler, self).__init__(*argc, **argkw)
        self.requestName = 'login'

    @tornado.gen.coroutine        
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
        if count != 0:
            code = self.return_code_process(count)

        else:
            phone = Data[self.user_module._user_phone]
            entity = self.user_module.get_info_from_phone(phone)
            if entity == []: 
                count += 1
                message = "the phone has not been register now."
                code = self.return_code_process(count)
                self.return_to_client(code,message)
                
            else:
                if Data[self._user_module._user_password] != entity[0][self._user_module._user_password]:
                    count += 2
                    message = "your input a wrong password"
                    code = self.return_code_process(count)
                    self.return_to_client(code,message)
                    
                else:
                    uid = str(entity[0][self.user_module._uid]) 
                    count += 3
                    result = self.redis_dict_check(str(uid), str(_xsrf))
                    # logging.info("login uid is %s _xsrf is %s result is %s"%(uid,_xsrf,result))
                    if result == 0:
                        message = "login successfully!"
                    elif result == 1:
                        count += 1
                        message = "login successfully! another user been logout!"
                    else:
                        count += 2
                        message = "you have login! needn't do it again!"
                    access_token = entity[0]['access_token']
                    uid = entity[0]['uid']
                    Data = self.user_detail_module.get_info_from_uid(uid)
                    # logging.info("data in mysql ac_user_detail_info is :%s"%Data)
                    # set cookie and dict
                    adlevel =entity[0][self.user_module._user_adlevel]
                    Data['adlevel'] = adlevel
#                    logging.info("login data is : %s"%Data)
 #                   logging.info("access_token %s     update time %s "%(access_token,Data['last_update_time']))
                    self.set_redis_dict(str(uid),_xsrf,access_token,Data['last_update_time'],adlevel)
                    self.message.init_message(uid)
                    self.set_secure_cookie('uid',str(uid))
                    code = self.return_code_process(count)
                    logging.info("data %s"%str(self.get_redis_dict(str(uid))))

                    self.return_to_client(code,message,Data)
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
            result = self.redis_dict_check(str(uid),str(_xsrf))
            if result == 0:
                message = "the account has been logout"
            elif result == 1:
                count = count + 1
                message = "_xsrf is wrong, can not logout"
            elif result == 2:
                count = count + 2
                message = "logout successfully!"
                last_update_time = self.get_user_last_update_time(uid)
                self.user_detail_module.update_last_update_time_by_uid(uid,last_update_time)
                self.delete_redis_dict(str(uid))
                self.clear_cookie('uid')
        self.return_code_process(count)
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
                "faculty":faculty,
                "major":major,
                "job":job,
                "uid":user_id,
                "publicity_level":0,
                "city":city,
                "real_name":real_name,
            'telephone': this parameter must be stored in client.
        [those field is used in Umeng update].
        "update_json":
            POST['icon_url']:
            POST['publicity_level']:
            POST['city']:
            POST['state']
            POST['country']
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
        count = 0
        uid = self.get_secure_cookie(self._user_module._uid)
        update_list = self.get_argument('list_info_has_update')
        # logging.info("update_list%s type is : %s"%(update_list,type(update_list)))
        
        if update_list == 0:
            DataJson = self.get_argument('info_json')
            Data = json.loads(DataJson)            
            count,message =self._check(Data)
            if count == 0:
                access_token = self.get_redis_dict(uid)[1]
                code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
                logging.info("in update_list to umeng")
        # update data to mysql
        if code != 0 or count != 0 :
            # request Umeng error!
            code = self.return_code_process(count)
            self.return_to_client(code,message)
            self.finish()
        else:
            update_dic = self.get_argument('update_json')
            update_dic = json.loads(update_dic)
            count,message = self._check(update_dic)
            if count == 0:
                # [todo]:add mysql operate error expection
                message = self.user_list_module.update_info_to_user(update_dic,uid)
                message = self.user_detail_module.update_info_to_user(update_dic,uid)
                message = self.elastic_user_module.updateinfo(update_dic,uid)
            code = self.return_code_process(count)
            self.return_to_client(code,message)
        # update data to elasticsearch
        self.elastic_user_module.updateinfo()

"""
Register admin user.
this method should been delete after the launch of ready-for-sale product
"""
class RegisterAdminHandler(UserHandler):
    def __init__(self, *argc, **argkw):
        super(RegisterAdminHandler, self).__init__(*argc, **argkw)
        self.requestName = 'register'
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
        code = 0
        jsonData = self.get_argument('info_json')
        pdb.set_trace()
        Data = json.loads(jsonData)
        count,message = self._check(Data)
        if count != 0:
            code = self.return_code_process(count)
            self.return_to_client(code,message)
            self.finish()
        else:
            phone = Data[self.user_module._user_phone]
            hasRegister = self.user_module.find_user_phone(phone)
            if hasRegister:
                count =count + 1 
                message = "User phone:%s has been register "%Data[self.user_module._user_phone]
            else:
                count = count + 1
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
                        stu_id,adlevel=1)
                    logging.info("after register code is %s message is %s"%(count,message))
                    # use update pai to set user's message.
                    # [todo]: should not write data to mysql before get successful information in umeng data.
                    self.url = '/0/user/update'
                    self.methodUsed = 'PUT'
                    self.requestName = 'update_user_info'
                    admission_year = Data[self.user_list_module._admission_year]
                    faculty = Data[self.user_list_module._faculty]
                    major = Data[self.user_list_module._major]
                    job = Data[self.user_list_module._job]
                    city = Data[self.user_list_module._city]
                    state = Data[self.user_list_module._state]
                    country= Data[self.user_list_module._country]
                    company = Data[self.user_detail_module._company]
                    real_name = Data[self._user_list_module._name]
                    phone = Data[self._user_module._user_phone]
                    custom = {
                    # "uni_id":1,# todo: uni_id == 1 ,prestent the SEU.
                    "admission_year":admission_year,
                    "faculty":faculty,
                    "major":major,
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
                        # code = self.return_code_process(count)
                        self.user_list_module.set_info_to_user(
                            user_id,admission_year,faculty_id,major_id,real_name,gender,job,icon_url,city,state,country)
                        self.user_detail_module.set_info_to_user(
                            user_id,admission_year,faculty_id,major_id,real_name,gender,job,icon_url,city,state,country,company)
                        self.user_message_module.set_user_to_message(user_id)
                        message = "register successfully!"
                        # logging.info('user_id :%s'%user_id)
            # encode message and code to json, send to client.
            self.return_to_client(code,message)
            self.finish()