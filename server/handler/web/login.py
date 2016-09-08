# login.py
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from common.variables import AP
class IndexWebHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('login.html')

class MainWebHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
