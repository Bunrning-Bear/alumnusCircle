# test.py
import os
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
import base64
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
class TestHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(TestHandler, self).__init__(*argc, **argkw)

    def post(self):
        info_json = self.get_argument('info_json')
        img = base64.b64decode(info_json)
        with open(os.path.join(r'/home/burningbear/temp/', 'temp.jpg'), 'wb') as file:
            file.write(img)
        # logging.info("type base64 is :%s"%chardet.detect(info_json))
        # info_json.decode('utf-8')
        # info_json.encode('base64')
        # arraylist = {'test':info_json}
        # logging.info("type base64 is :%s"%arraylist)

       # self.write(data)


    # def post(self):
    #     info_json = self.get_argument('info_json')
    #     img = base64.b64decode(info_json)
    #     with open(os.path.join(r'/home/temp/', 'temp.jpg'), 'wb') as file:
    #         file.write(img)

        # logging.info("type base64 is :%s"%chardet.detect(info_json))
        # info_json.decode('utf-8')
        # info_json.encode('base64')
        # arraylist = {'test':info_json}
        # logging.info("type base64 is :%s"%arraylist)
