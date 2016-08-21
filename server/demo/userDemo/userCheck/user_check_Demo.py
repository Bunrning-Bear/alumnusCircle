# -*- coding: utf-8 -*-
#user_check_Demo.py
"""
使用安全cookie标志用户
当首次在某个客户端[或者cookie过期]访问我们的页面的时候，展示的一个登陆页面。
TODO:-----更新到期时间
登陆界面通过POST方法提交表单，POST的body通过调用set_secure_cookie()来存储username中求其请参数中的提交值
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import os.path

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        """
    	从客户端获取cookie中 的username的值
    	"""
        return self.get_secure_cookie("username")


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        self.set_secure_cookie("username",self.get_argument("username"))
        self.redirect("/")

class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated#???
    def get(self):
        self.render('index.html',user=self.current_user)


class LogoutHandler(BaseHandler):
    def get(self):
        if (self.get_argument("logout",None)):
            self.clear_cookie("username")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    settings ={
        "template_path": os.path.join(os.path.dirname(__file__),"templates"),
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "xsrf_cookies": True,
        "login_url": "/login"
    }
    application = tornado.web.Application([
            (r'/',WelcomeHandler),
            (r'/login',LoginHandler),
            (r'/logout',LogoutHandler)
        ],**settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()