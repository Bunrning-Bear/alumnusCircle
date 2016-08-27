# -*- coding: utf-8 -*-
# login.py
import random
import json
import struct
import base64
import urllib
import tornado.httpclient

import ConfigParser

import encrypted
## TODO: sys should been locate to another place.
import sys
location = '/home/burningbear/CodePlace/python/web/alumnusCircle/server/'
sys.path.append(location)
from common.variables import USER_DICT



class RegisterHandler(object):

    def __getUserData(self):
        """
		     # get data from mysql.
    	  `user_id` int(8) NOT NULL COMMENT '用户id',
          `user_name` varchar(50) DEFAULT NULL COMMENT '用户昵称',
          `user_passwd` varchar(100) DEFAULT NULL COMMENT '用户密码',
          `user_phone` varchar(20) DEFAULT NULL COMMENT '用户电话号码',
          `user_qq_id` varchar(20) DEFAULT NULL COMMENT '用户QQ号',
          `user_wechat_id` varchar(20) DEFAULT NULL COMMENT '用户微信号'
        """
        randomNum = str(random.randint(1,1000))
        user_name = "virtual_admin"
        icon_url = "http://umeng.com/1.jpg"
        user_id = str(-1)
        source = "self_account"
        data = {"user_info":{"name":user_name,"icon_url":icon_url},"source_uid":user_id,"source":source} 
        data = json.dumps(data)
        data = struct.pack(">I",len(data)) + data
        return data

    def __get_encrypted_data(self):
        data = self.__getUserData()
        data = encrypted.prpcrypt("224477ddffb25d994302d4b0c7b87482").encrypt(data)
        encrypted_data = base64.b64encode( data )
        return encrypted_data

    def register(self):
        prefix = "https://rest.wsq.umeng.com"
        encrypted_data = self.__get_encrypted_data()
        url = prefix+"/0/get_access_token?ak=" + "57b18b2ee0f55ac368001dc8"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    	  
        body = urllib.urlencode({"encrypted_data":encrypted_data})
        client = tornado.httpclient.HTTPClient()

        request = tornado.httpclient.HTTPRequest(
            url=url,
            method="POST",
            headers=headers,
            body=body
        )
        response = client.fetch(request)
        body =  json.loads(response.body)
        return str(body)
         #{"err_msg": "user name is duplicated", "err_code": 10013}
        """
        TODO: how to dispose error.

	    10001 	user base info is not complete 	
		10002 	user does not exist 	
		# 110003 	user did not log in 	
		# 10004 	user don't have privilege to do this. 	
		10005 	user identity is invaild 	
		10006 	user has been created 	
		# 10007 	user has been followed 	
		10008 	user login info not complete 	
		# 10009 	user cannot follow self 	
		10010 	user name length should be in range 2,20 	
		10011 	user is unusable: deleted or forbidden 	
		10012 	user name contains sensitive words 	
		10013 	user name is duplicated 	
		10014 	user custom length should be in range 0, 50 	
		10015 	this operation only allows one user per time 	
		10016 	user name contains illegal characters
		"""
        # success: return this data to php and add it to sql.
    #    return "access_token is :"+body['access_token']


"""
 now suppose i has get a access_token from mysql, I want to login now.
{   
	"id": "579e0b08b9a996088bace535", 
	"source_uid": "406", 
	"source": "self_account", 
	"name": "Burningbear406", 
	"age": null,
     "gender": 0, 
     "atype": 0, 
     "status": 0, 
     "icon_url": {
     	"origin": "http://umeng.com/1.jpg", 
     	"640": "http://umeng.com/1.jpg", 
     	"240": "http://umeng.com/1.jpg", 
     	"format": "unknown"
     	}, 
     "level": 0, 
     "level_title": "", 
     "score": 0, 
     "access_token": "91ecfda554562b067956f6a8ae927d288dd96616acf8f6427bf95cb267bb069deeadfda4432fa1ac82a0cef16f65b40598d359c15cad20ced3d8c375b0c1b122"
 }
"""
class LogHandler(object):
	def login(self,user_id,session,access_token):
		# self.application.session will be a dictory which store all of login user.
		# add user to dictory
		# demo:
		# d.get('Thomas', -1)
		# delete: d.pop('Bob')
		result = USER_DICT.get(user_id,-1)
		if result == -1:
			USER_DICT[user_id] = (access_token,session)
		elif result[1] != session:
			print "invaild login"
		else:
			print "has login"

		return USER_DICT

	def logout(self,user_id,access_token):
		pass

if __name__ == '__main__':
	# register
    registerObj = RegisterHandler()
    # get user information as patameter, return access_token to mysql.
    access = registerObj.register()
    loginObj = LogHandler()
    user_id = "406"
    access_token = "635755b350420c81c446da313733de1efd666c2fb56f49a3ef2da01345cb81f7b7501f95fab96fea6c98f926c28da46a192420aa93389f91d8cd777f493abd63"
    userDict = loginObj.login(user_id,1234,access_token)
    #print "userDict"
    #print userDict
    print "access_token"
    print access
    # 91ecfda554562b067956f6a8ae927d288dd96616acf8f6427bf95cb267bb069d17a74a7c5d2c78aed60572e4f127099f1db4065e88f7fce65df0ef51e28bc96f
    # 91ecfda554562b067956f6a8ae927d288dd96616acf8f6427bf95cb267bb069d7a6559d5d9412dfa4f1857545caadb692f23551e649944fb6abd89c6f55a5b18
    