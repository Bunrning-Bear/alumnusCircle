#!/usr/bin/env python
# coding=utf-8
#server_client_async.py
import urllib 
import json 
import datetime 
import time 
import logging
import random
import tornado.httpserver 
import tornado.ioloop 
import tornado.options 
import tornado.web 
import tornado.httpclient 
import tornado.gen
import ConfigParser


logging.basicConfig(level=logging.INFO)

from tornado.options import define, options 
define("port", default=8001, help="run on the given port", type=int) 
def get_xsrf():
    config = ConfigParser.ConfigParser()
    config.readfp(open('global.ini'))
    return config.get('client','_xsrf')

def set_cookie(resp):
    headers = resp.headers.get_list('Set-Cookie')
    config = ConfigParser.ConfigParser()
    config.readfp(open("global.ini"))
    config.set('client','cookie',headers)
    config.write(open('global.ini',"w"))
    return headers

def request(Data,methodused,api):
    url = "http://localhost:8000" + api
    body = urllib.urlencode(Data)
    config = ConfigParser.ConfigParser()
    config.readfp(open('global.ini'))
    cookie = config.get('client','cookie')
    headers = {
    "Cookie":cookie,
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    client = tornado.httpclient.HTTPClient()
    logging.info("in request")

    if methodused =='GET':
        if body:
            url = url +"&"+ body
            body = ''
        else:
            url = url
        request = tornado.httpclient.HTTPRequest(
            url=url,
            method=methodused,
            headers=headers
        )        
    else:
        request = tornado.httpclient.HTTPRequest(
            url=url,
            method=methodused,
            body=body,
            headers=headers
        )
    logging.info("body %s url %s headers %s"%(str(body),str(url),str(headers)))
    response = client.fetch(request)

    return response

def packJson(dic):
        info_json = json.dumps(dic)
        data ={
        "_xsrf":get_xsrf(),
        "info_json":info_json
        }
        return data


class IndexHandler(tornado.web.RequestHandler): 
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self): 
        body = request({},"GET","/")
        config = ConfigParser.ConfigParser()
#        config.readfp(open('global.ini'))
#        config.set('cookie','_xsrf',body['_xsrf'])
#        config.write(open('global.ini','w'))
        self.write("return test is :%s"%body)
        self.finish()

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        url = "/register"
        # ref: http://blog.jobbole.com/96052/
        # phone number begin with 13 or 14 or 15 or 17 or 18, 
        # length allowed is: 11.
#        self._regex_dict[self.user_module._user_phone] = ur"^13[\d]{9}$|^14[5,7]{1}\d{8}$|^15[^4]{1}\d{8}$|^17[0,6,7,8]{1}\d{8}$|^18[\d]{9}$\Z"
        # begin with letter, length between 6 and 18, all allowed char are letter, number and underline.
        # length allowed is: 6 to 18

#        self._regex_dict[self._user_module._user_password] = ur"^[a-zA-Z]\w{5,17}$\Z"
        # username should been decode with 'utf8',all allowed are chinese char, letter, number and underline.
        # length allowed is: 6 to 16
#       self._regex_dict[self._user_module._user_name] = ur"^[\u4e00-\u9fa5\w]{6,15}$\Z"
        # the smallest qq id is 10000
#        self._regex_dict[self._user_module._user_qq] = ur"[1-9][0-9]{4,}\Z"
        # wechat id can be letter, number and underline
#        self._regex_dict[self._user_module._user_wechat] = ur"^[\w]{5,}$\Z"        
        dic = {}
        testType = {}
        # test user name.
        num = 0
        dic[num] ={
        "user_name":"12345",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="</br>start test username.</br>5 chars user name,should be error"
        num = num + 1
        dic[num] ={
        "user_name":"123456",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="equal to 6 chars user name,OK "
        num = num + 1

        dic[num] ={
        "user_name":"1234578901234567",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="17 chars user name,error"
        num = num + 1
        dic[num] ={
        "user_name":"12345789012345678",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="18 chars user name,error"        
        num = num + 1
        dic[num] ={
        "user_name":"123457890123456",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="equal to 16 chars user name,ok"        
        num = num + 1
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="chinese char in user name,ok"    
        num = num + 1         
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="duplicate user name. [todo]:should not be succeed."       
        num = num + 1 

        # password test
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="</br>start test password.</br>start with number,error"
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"z1995",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="less than 6 chars[5 chars],error"
        num = num + 1
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"z1234567890123456",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="longer than 16 chars[17 chars],error"
        num = num + 1
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp.19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="use special chars,error"
        num = num + 1

        # phone test
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"101961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="</br>start test phone_id.</br>start with 10[not 13 14 15,17,18],error"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"15196"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="less than 11 digits[10 digits],error"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"1519611"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="more than 11 digits[12 digits],error"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"A151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="chars appear,error"
        num = num + 1        
        # test qq_id
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="</br>start test qq_id.</br>empty,ok"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"9999",
        "user_wechat_id":""
        }
        testType[num]="less than 10000[9999],error"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"471326290",
        "user_wechat_id":""
        }
        testType[num]="qq=471326290,ok"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"a134556",
        "user_wechat_id":""
        }
        testType[num]="char appear,error"
        num = num + 1        
        # wechat test
        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":"adfghd."
        }
        testType[num]="</br>wechat test .</br>use special chars[adfgh.],error"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":"asdd"
        }
        testType[num]="less than 5 chars [asdd] ,error"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"151961"+str(random.randint(10000,99999)),
        "user_qq_id":"",
        "user_wechat_id":"zpcxh95"
        }
        testType[num]="wechat = zpcxh95,ok"
        num = num + 1        
        dic[num] ={
        "user_name":"6个中文字符呢",
        "user_passwd":"zp19950310",
        "user_phone":"15195861108",
        "user_qq_id":"",
        "user_wechat_id":""
        }
        testType[num]="</br>register phone test .</br>phone has been register,error"
        num = num + 1
        count = 0
        while count < len(dic):
            data = packJson(dic[count])
            resp = request(data,"POST",url)
            body = json.loads(resp.body)   
            cookie =set_cookie(resp)
            self.write("login type: %s ----</br> result:%s </br>cookie：%s</br></br>"%(testType[count],body,cookie))
            count = count + 1

class LogintestHandler(tornado.web.RequestHandler):
    def get(self):
        url = "/login"
        dic = {}
        num = 0
        testType = {}
        dic[num] ={
        "user_passwd":"zp19950310",
        "user_phone":"15196197203",
        }
        testType[num]="</br>login test .</br> 15196197203.zp19950310.ok"
        num = num + 1
        dic[num] ={
        "user_passwd":"zp19950310",
        "user_phone":"15196197203",
        }
        testType[num]="17195861108 login again!.error"
        num = num + 1
        dic[num] ={
        "user_passwd":"zp19950310",
        "user_phone":"17195861108",
        }
        testType[num]="17195861108[not register],error"
        num = num + 1
        dic[num] ={
        "user_passwd":"zp199503101",
        "user_phone":"15195861108",
        }
        testType[num]="password error,error"
        num = num + 1
        count = 0
        while count < len(dic):
            data = packJson(dic[count])
            resp = request(data,"POST",url)
            body = json.loads(resp.body)   
            cookie =set_cookie(resp)
            self.write("login type: %s ----</br> result:%s </br>cookie：%s</br></br>"%(testType[count],body,cookie))
            count = count + 1

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        url = "/login"
        dic = {}
        num = 0
        testType = {}
        dic[num] ={
        "user_passwd":"zp19950310",
        "user_phone":"15196197203",
        }
        testType[num]="</br>login test .</br> 15196197203.zp19950310.ok.this is test acount"
        count = 0
        while count < len(dic):
            resp = request({},"GET","/")
            body = json.loads(resp.body)   
            cookie1 =set_cookie(resp)
            data = packJson(dic[count])
            resp = request(data,"POST",url)
            body = json.loads(resp.body)   
            cookie =set_cookie(resp)
            self.write("login type: %s ----</br> result:%s </br>cookie1：%s</br> cookie:%s</br></br>"%(testType[count],body,cookie1,cookie))
            count = count + 1


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        url = "/logout"
        dic ={}
        testType = {}
        num = 0
        testType[num] = ""
        dic[0] = {}
        count = 0
        while count < len(dic):
            data = packJson(dic[count])
            resp = request(data,"POST",url)
            body = json.loads(resp.body)   
            cookie =set_cookie(resp)
            self.write("logout type: %s ----</br> result:%s </br>cookie：%s</br></br>"%(testType[count],body,cookie))
            count = count + 1

if __name__ == "__main__": 
    tornado.options.parse_command_line() 
    app = tornado.web.Application(
        handlers=[
        (r"/", IndexHandler),
        (r"/register",RegisterHandler),
        (r"/logintest",LogintestHandler),
        (r"/login",LoginHandler),
        (r"/logout",LogoutHandler)
        ])
    http_server = tornado.httpserver.HTTPServer(app) 
    http_server.listen(options.port) 
    tornado.ioloop.IOLoop.instance().start()