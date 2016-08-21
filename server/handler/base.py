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
import urllib
import tornado.web
import tornado.gen
import tornado.httpclient

from common.lib.prpcrypt import set_encrypt

from common.variables import AP,CODE_DICT


def authenticated(request):
    """
    This is a decorator for all of request process function which login is needed.

    authenticated will check if the request has the same _xsrf in server.
    authenticated will check the _xsrf in user_dict after then.

    Args:
        request:[string] is the request name such as "logout".
        Look for papacamera/common/variables for detail
    
    Returns:
        If server did not find current_user in client (look get current_user function for detail),
        server will return a error code instand of execute its statement.
    """
    def decorator(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):            
#[todo] can target add to request? 
#          logging.info("client xsrf is %s server xsrf is: %s"%(_xsrf,self.xsrf_token))
#            try:
#                target = self.get_argument('target')
#           except tornado.web.MissingArgumentError, e:
#               logging.info("not argument target, continue")
#               target = ""
            if not self.current_user:
                code = self.return_code_process(request,29) 
                message = "your login information has been cleared or you have not login when you are tring to "+ request
                self.return_to_client(code,message)
                self.finish()
                return
            else:
                uid = self.get_secure_cookie('uid')   
                code,message = self.request_identifier_check(uid,self.requestName)
                # code == 3,means it is the real user.
                if code != 3:
                    code = self.return_code_process(self.requestName,code)
                    self.return_to_client(code,message)
                    self.finish()
                    return
                else:
                    return method(self,*args, **kwargs)
        return wrapper
    return decorator

def public_access_decorator(method):
    """This decorator should be use in all of public access to umeng.

    This decorator will check if public access token in server has outdate.
    Then change it and request again if outdate

    Args:
        method:[generator] should be a generator, this generator will return code and message
        when code == 50005, it means the public access has outdate.

    Returns:
        return the code and message after get the new public access token.
    """
    @tornado.gen.coroutine
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        again = 1
        while again>=0 and again <= 10:
            code = 0
            message = ''            
            config = ConfigParser.ConfigParser()
            config.readfp(open(AP+'/common/conf.ini'))
            self._public_access = config.get('app','public_access')
            access_token = self._public_access
            logging.info("public access in decorator: %s"%(access_token))
            (code,message) = yield method(self, *args, **kwargs)
            logging.info("code: %s message : %s. agin = %s"%(code,message,again))
            if code == 50005:
                again = again + 1
                get_times = 1
                while get_times <=10:
                    get_times = self.update_public_access_token(get_times,access_token)
                    if get_times == 0:
                        logging.info("in get times == 0 ")
                        break
            else:
                again = -1
        if again == 11:
            code = 1
            message = "get public access token error, please requset latter"
            
        raise tornado.gen.Return((code,message))
    return wrapper


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self._db = self.application.db
        self._user_dict = self.application._user_dict
        # load all of variable needed into BaseHandler.
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'/common/conf.ini'))
        self._aes_key = config.get('app','secret')
        self._appkey = config.get('app','appkey')
        self._prefix = config.get('url','prefix')
        self._public_access = config.get('app','public_access')
        # load all of module operate into BaseHandler.
        self._user_module = modules.user.UserInfoModule(self._db)
        self._user_list_module = modules.user.UserListModule(self._db)
        self._user_detail_module = modules.user.UserDetailModule(self._db)
        self._code_dict =CODE_DICT         

    @property
    def user_module(self):
        return self._user_module

    @property    
    def user_list_module(self):
        return self._user_list_module

    @property
    def user_detail_module(self):
        return self._user_detail_module

    def get_current_user(self):
        """
        If this function return None 0 or [], function which has decorator
        "@tornado.web.authenticated" will redirect to the Handler login_url
        has define.
        """
        return self.get_secure_cookie("uid")
    # [todo]2016.8.4 user_dict should been store in redis   
    def user_dict_check(self,uid,_xsrf):
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
        if not self._user_dict.has_key(uid):
            return 0
        elif self._user_dict[uid][0] != _xsrf:
            return 1
        else:
            return 2

    def set_user_dict(self,uid,_xsrf,access_token):
        self._user_dict[uid]=(_xsrf,access_token)

    def get_user_dict(self,uid):
        return self._user_dict[uid]

    def delete_user_dict(self,uid):
        del self._user_dict[uid]

    def return_code_process(self,handler,code):
        """Return status code to client after get a code from handler.

        Args:
        handler:[string] must be a name of handler such as "reigster" or "login"
        code: [int] status code in a handler.

        Returns:
        [string] global status code.
        """
        return self._code_dict[handler] + code


    def update_public_access_token(self,times,old_token):
        """When public access token was outdate, we will call this function.
            
        server will request Umeng server to get a new public access token to user.
        
        Args:
            times[int]:record request times to Umeng.
                To avoid request too much times to Umeng and did not get a new public access token.
            old_token[sting]:pass the public access_token before call this function.
                to Avoid too much user request public access_token together.
                This function will ignore requests after public access_token 
                has been updated by other request before.
        
        Returns:
            public access token:this function will store new public access token [if get it] to self._public_access
            times: if get new access token, return times = 0, else return times = times + 1.

        """
        code = 0
        message = ''
        result = times + 1
        #When a new public_access_token get, server will ignore update operate after it.
        logging.info("self public access: %s old token %s"%(self._public_access,old_token))
        if self._public_access == old_token:
            data = {}
            cryptedData = set_encrypt(self._aes_key,data)
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
            response = client.fetch(request)
            body =  json.loads(response.body)
            code,message = self.set_UmengCode(code,body)
            logging.info("in get public access token:code :%s message:%s </br> body is: %s"%(code,message,body))
            if 'access_token' in body:
                result = 0
                self._public_access = body['access_token']
                config = ConfigParser.ConfigParser()
                config.readfp(open(AP+'/common/conf.ini'))
                config.set('app','public_access',self._public_access)
                config.write(open(AP+'/common/conf.ini',"w"))
                logging.info("access_token in body and self.public_access = %s"%self._public_access)
                new_access = config.get('app','public_access')
                logging.info("new access : %s"%new_access)
            return result
        else:
            return 0

    def set_UmengCode(self,count,body):
        code = 0
        message = ''
        if "err_code" in body:
            code = body['err_code']
            message = body['err_msg']
        else:
            message = body               
            code = self.return_code_process(self.requestName,count)
        return code,message

    @tornado.web.asynchronous
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
        if Data == {}:
            resultJson = json.dumps({'code':code,'message':message,'Data':'{}'})
        else:
            Data = json.dumps(Data)
            resultJson = json.dumps({'code':code,'message':message,'Data':Data})
        self.write(resultJson) 



class UploadFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
<html>
  <head><title>Upload File</title></head>
  <body>
    <form action='/uploadfile' enctype="multipart/form-data" method='post'>
    <input type='file' name='file'/><br/>
    <input type='submit' value='submit'/>
    </form>
  </body>
</html>
''')

    def post(self):
        upload_path=os.path.join(os.path.dirname(AP),'files')  #文件的暂存路径
        file_metas=self.request.files['Filename']    #提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename=meta['filename']
            filepath=os.path.join(upload_path,filename)
            with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])
            self.write('finished!')