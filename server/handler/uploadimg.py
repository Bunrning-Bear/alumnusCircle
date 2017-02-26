#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author Zhengfan
#Date 16.08.29
#Version 1.0
#Function The base class of the upload image classes.
#Note We suppose to use the Aliyun Service.

import tornado
import tornado.httpclient
import tornado.httpserver
import tornado.web
import tornado.gen


import modules
from modules import uploadimg

class UploadImgHandler(tornado.web.RequestHandler):
	def __init__(self, *arg, **argkw):
		super(UploadImgHandler, self).__init__(*arg, **argkw)
		self.db = self.application.db
		self.imageCache = uploadimg.ImageCache()
		self.executeSQL = uploadimg.ExecuteSQL()
		self.aliyun = uploadimg.Aliyun()
