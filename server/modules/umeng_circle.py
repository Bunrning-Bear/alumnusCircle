#!usr/bin/env python
# coding=utf-8
# umeng_circle.py
import ConfigParser
from base import BaseModule
from common.variables import AP
from handler.request import RequestHandler
"""
    1. user apply a circle.
    2. create a new message.
    3. circle admin reject or agree this applyer.
    4. agree:
        user follow this cricle in umeng.
        user add mysql: my_circle_list to mysql.
"""
class UmengCircleModule(RequestHandler):
    def __init__(self,db):
        RequestHandler.__init__(self,db)
        
        
    def followCircle(self,access_token):


