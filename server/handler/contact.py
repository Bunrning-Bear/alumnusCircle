#!/usr/bin/env python
# coding=utf-8
# contact.py
"""
contact :
    1. get all of user in elasticsearch.
    2. filter by all of user.
    3. keyword search.
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

import user
import base
import request
import modules.review_deal
import modules.circle
from common.lib.prpcrypt import prpcrypt,set_encrypt
from common.lib.to_list import custom_list_to_list
from request import RequestHandler
from base import BaseHandler

"""
    base handler of cantact part.
"""
class ContactHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(ContactHandler, self).__init__(*argc, **argkw)
        # self._elastic_user_module 
"""
    Get All of User in Our App. and you can filter it through pass some parameter.
"""
class AllUserFilterHandler(ContactHandler):
    def __init__(self, *argc, **argkw):
        super(AllUserFilterHandler, self).__init__(*argc, **argkw)      

    def post(self):
        