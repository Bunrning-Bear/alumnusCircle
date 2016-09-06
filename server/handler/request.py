#request.py
"""
request.py define RequestHandler, 
which is parents class for all of request handler except login and open app
"""
import ConfigParser
import logging
import json
import urllib
import functools

import base
import tornado.web
import tornado.gen
import tornado.httpclient

from common.lib.prpcrypt import set_encrypt
from base import BaseHandler
from common.variables import AP,CODE_DICT


def authenticated(request):
    """
    This is a decorator for all of request process function which login is needed.

    authenticated will check if the request has the same _xsrf in server.
    authenticated will check the _xsrf in redis_dict after then.

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
                code = self.return_code_process(29) 
                message = "your login information has been cleared or you have not login when you are tring to "+ request
                self.return_to_client(code,message)
                self.finish()
                return
            else:
                uid = self.get_secure_cookie('uid')   
                code,message = self.request_identifier_check(uid,self.requestName)
                # code == 3,means it is the real user.
                if code != 3:
                    code = self.return_code_process(code)
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
            (code,message,Data) = yield method(self, *args, **kwargs)
            logging.info("code: %s message : %s. again = %s"%(code,message,again))
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
            
        raise tornado.gen.Return((code,message,Data))
    return wrapper


class RequestHandler(BaseHandler):
    def __init__(self, *argc, **argkw):
        super(RequestHandler, self).__init__(*argc, **argkw)
        self.count = 10
        self.requestName ='default'
        self.message = self.application.message
        
    def get_optional_argument(self,argu):
        try:
            result = self.get_argument(argu)
        except tornado.web.MissingArgumentError,e:
            result = NULL
        finally:
            return result

    def set_Umeng_request(self,request,access_token,Data,method):
        url = self._prefix + request + "?ak="+ self._appkey + "&access_token="+ access_token
        body = urllib.urlencode(Data)
        if method =='GET':
            request = url +"&"+ body
            request = tornado.httpclient.HTTPRequest(request)
        else:
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }
            # logging.info("body is : %s "%body)
            request = tornado.httpclient.HTTPRequest(
                url=url,
                method=method,
                headers=headers,
                body=body,
                allow_nonstandard_methods=True
            )
        logging.info("url of set_umengrequest:%s"%url)
        return request

    @tornado.gen.coroutine
    def Umeng_asyn_request(self,access_token,Data): 
        """This is an function encapsulate the process server send a request to Umeng server.

        before call this function:
            you should assign umeng's url preix to self.url 
            [don't include parameter an its value(it should been in 'Data')].
            you should assign umeng's url's method to self.methodUsed.
            you should assign request name string to self.requestname

        Args:
            access_token:[string] user's access_token.
            Data:[dictory] just set all of key-value [include parameter and value in GET method]

        Returns:
            return code and message, see detail in set_UmengCode(code,body,Data)
        """
        client = tornado.httpclient.AsyncHTTPClient()
        code = 0
        message = ''
        request = self.set_Umeng_request(self.url,access_token,Data,self.methodUsed)
        logging.info("Umeng_asyn_request request is :")
        logging.info(', '.join(['%s:%s' % item for item in request.__dict__.items()]))
        response = yield tornado.gen.Task(client.fetch,request)
        body =  json.loads(response.body)
        code,message,Data = self.set_UmengCode(body)
        raise tornado.gen.Return((code,message,Data))
 
    @public_access_decorator
    @tornado.gen.coroutine
    def public_Umeng_request(self,access_token,Data):
        """This request is use to send all of feed request to Umeng which login is not need 
        """
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'/common/conf.ini'))
        self._public_access = config.get('app','public_access')
        access_token = self._public_access        
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)           
        raise tornado.gen.Return((code,message,Data))

    """
    def is_from_the_same_client(self,request, uid, _xsrf):
        """"""
        [delete]
        This function is to check the identifier from user, 
        [2016.6.8] this function has been replaced by function request_identifier_check       
        Args:
            request:[string] is the request name such as "upload_feed".
            Look for papacamera/common/variables for detail
            count:[int] the error code number befor the_same_client function was call.
            uid:[string] user id get from client's cookie.
            _xsrf:[string] _xsrf cookie get from client.
        Returns:
            Only if redis_dict[uid][0] == _xsrf, that we can confirm that the request come from the real user
            unless the request should not execute excepte return a error code.
        """"""
        code = 0
        result = self.redis_dict_check(uid,_xsrf)
        message = ''
        if result == 0:
            count = 1
            message = "your cookie has been cleared (maybe you has logout or change your password) when " + request
        elif result == 1:
            count = 2
            message = "there are others has login your account, please change your password now !"
        else:
            code = 3
            message = "your are the real user, this message will not return to client in normal."
        return code, message   
    """
    def request_identifier_check(self,uid,request_name):
        """This function is to check the identifier from user, though compare uid and redis_dict 
        
        Args:
            request_name:[string] is the request name such as "upload_feed".
            Look for ~/common/variables for detail
            uid:[string] user id get from client's cookie.

        Returns:
            Only if redis_dict[uid][0] == _xsrf, that we can confirm that the request come from the real user
            unless the request should not execute excepte return a error code.
        """
        _xsrf = self.get_argument('_xsrf')
        count = 0
        message = ''
        result = self.redis_dict_check(uid,_xsrf)
        message = ''
        if result == 0:
            count =1
            message = "your cookie has been cleared (maybe you has logout or change your password) when " + request_name
        elif result == 1:
            count = 2
            message = "there are others has login your account, please change your password now !"
        else:
            count = 3
            message = "your are the real user, this message will not return to client in normal."
        return count, message

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
            code,message,Data = self.set_UmengCode(body)
            logging.info("in get public access token:code :%s Data:%s </br> body is: %s"%(code,Data,body))
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

    def set_UmengCode(self,body):
        """analyse the return body of umeng and get the return code if has error.

        Args:
            body: the message response from umeng.

        Returns:
            if has error code: 
                function will return error code, error message and empty Data.
            if success:
                will return 0 code, success message, and body as Data.

        """
        code = 0
        message = ''
        if "err_code" in body:
            code = body['err_code']
            message = body['err_msg']
            Data = {}
        else:
            message = "get umeng api successfully"              
            code = 0
            Data = body

        return code,message,Data