#request.py
"""
request.py define RequestHandler, 
which is parents class for all of request handler except login and open app
"""
import ConfigParser
import logging
import json
import urllib

import base
import tornado.web
import tornado.gen
import tornado.httpclient

from common.lib.prpcrypt import set_encrypt
from base import BaseHandler
from common.variables import AP,CODE_DICT

class RequestHandler(BaseHandler):
    def __init__(self, *argc, **argkw):
        super(RequestHandler, self).__init__(*argc, **argkw)
        self.count = 10
        self.requestName ='default'

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
    

    # encode message and code to json, send to client. 

#    @public_access_decorator
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
            return code and message, see detail in set_UmengCode(code,body)
        """
        client = tornado.httpclient.AsyncHTTPClient()
        code = 0
        message = ''
        request = self.set_Umeng_request(self.url,access_token,Data,self.methodUsed)
        logging.info("Umeng_asyn_request request is :")
        logging.info(', '.join(['%s:%s' % item for item in request.__dict__.items()]))
        response = yield tornado.gen.Task(client.fetch,request)
        body =  json.loads(response.body)
        code,message = self.set_UmengCode(code,body)
        raise tornado.gen.Return((code,message))

    @base.public_access_decorator
    @tornado.gen.coroutine
    def public_Umeng_request(self,access_token,Data):
        """This request is use to send all of feed request to Umeng which login is not need 
        """
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'/common/conf.ini'))
        self._public_access = config.get('app','public_access')
        access_token = self._public_access        
        code,message =yield self.Umeng_asyn_request(access_token,Data)           
        raise tornado.gen.Return((code,message))

    def umeng_Api(self,request,access_token,Data,count,method):
        """
        [delete]
        This is Api from python to Umeng api
        [this function was replaced by set_UmengRequest and setUmengCode for asyn operate.]
        """
#        logging.info("now in update feed ,access_token is : %s"%(access_token))
        code = 0
        message = ''
        url = self._prefix + request + "?ak="+ self._appkey + "&access_token="+ access_token
#        logging.info("url is :%s"%url)
        body = urllib.urlencode(Data)
        client = tornado.httpclient.HTTPClient()        
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
            #logging.info("httpRequest: %s"%dir(request))
            #logging.info(', '.join(['%s:%s' % item for item in request.__dict__.items()]))
#        code,message = client.fetch(request, callback=self.on_response) 
        response = client.fetch(request)
 #       logging.info("response: %s"%response)
        body = json.loads(response.body)
        if "err_code" in body:
            code = body['err_code']
            message = body['err_msg']
        else:
            message = body               
#             code,message = yield self.umeng_Api(request,access_token,Data,count,"POST")
        if code == 0:
            code = self.return_code_process('update',count)
        return code,message  

    def is_from_the_same_client(self,request, uid, _xsrf):
        """
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
            Only if user_dict[uid][0] == _xsrf, that we can confirm that the request come from the real user
            unless the request should not execute excepte return a error code.
        """
        code = 0
        result = self.user_dict_check(uid,_xsrf)
        message = ''
        if result == 0:
            count =1
            message = "your cookie has been cleared (maybe you has logout or change your password) when " + request
        elif result == 1:
            count = 2
            message = "there are others has login your account, please change your password now !"
        else:
            code = 3
            message = "your are the real user, this message will not return to client in normal."
        return code, message   

    def request_identifier_check(self,uid,request_name):
        """
        This function is to check the identifier from user, though compare uid and user_dict 
        """
        _xsrf = self.get_argument('_xsrf')
        count = 0
        message = ''
        result = self.user_dict_check(uid,_xsrf)
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