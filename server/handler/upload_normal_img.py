#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author Zhengfan
#Date 16.09.10
#Version 1.0
#Function Provides the function that clients upload their images without uid or cid.
#Note inherit uploadimg.UploadImgHandler()

import os
import time
import json
import base64

import tornado
import tornado.httpclient
import tornado.httpserver
import tornado.web
import tornado.gen

import handler
from handler import uploadimg
from uploadimg import UploadImgHandler

class UploadNormalImgHandler(UploadImgHandler):
	def __init__(self, *arg, **argkw):
		super(UploadNormalImgHandler, self).__init__(*arg, **argkw)
		self.keyPrefix = r'http://www.seu.edu.cn/'
		self.cachePath = r'/home/chine/Disk/work/server/temp/'


	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def get(self):
		try:
			result = json.dumps({
			"code":74138
			,"message":"Hello, Welcome to upload your image !"
			,"img_key":"empty"
			,"img_url":"empty"
			})
			self.write(result)
		except:
			pass
		finally:
			self.finish()


	# #with local cache.
	# @tornado.web.asynchronous
	# @tornado.gen.coroutine
	# def post(self):
	# 	try: 
	# 		random_num = self.get_argument('random_num')
	# 		if(random_num == None):
	# 			random_num = '0123456789'
	# 		base64ImgStr = self.get_argument('base64ImgStr')
	# 		if(base64ImgStr == None):
	# 			raise
	# 		currentTime = time.time()
	# 		key = random_num + str(currentTime) + '.jpg'
	# 		fakeKey = self.keyPrefix + key
	# 		localCacheAbsolutePath = os.path.join(self.cachePath, key)
	# 		self.imageCache.saveBase64ImgStr(localCacheAbsolutePath, base64ImgStr)
	# 		self.aliyun.uploadImgFile(key, localCacheAbsolutePath)
	# 		img_url = self.aliyun.parseUrlByKey(key)
	# 		result = json.dumps({
	# 				"code":600
	# 				,"message":"Upload Image Successfully !"
	# 				,"img_key":fakeKey
	# 				,"img_url":img_url
	# 				})
	# 		self.write(result)
	# 	except:
	# 		result = json.dumps({
	# 			"code":601
	# 			,"message":"I'm sorry about that you are faild to upload image."
	# 			,"img_key":"empty"
	# 			,"img_url":"empty"
	# 			})
	# 		self.write(result)
	# 	finally:
	# 		self.finish()


	#without local cache, upload to cloud server directly.(This is a better choice)
	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def post(self):
		try: 
			random_num = self.get_argument('random_num')
			if(random_num == None):
				random_num = '0123456789'
			base64ImgStr = self.get_argument('base64ImgStr')
			if(base64ImgStr == None):
				raise
			imgBytes = base64.b64decode(base64ImgStr)
			currentTime = time.time()
			key = random_num + str(currentTime) + '.jpg'
			fakeKey = self.keyPrefix + key
			self.aliyun.uploadImgBytes(key, imgBytes)
			img_url = self.aliyun.parseUrlByKey(key)
			result = json.dumps({
					"code":600
					,"message":"Upload Image Successfully !"
					,"img_key":fakeKey
					,"img_url":img_url
					})
			print "Here"
			self.write(result)
		except Exception,e:
			print e
			result = json.dumps({
				"code":601
				,"message":"I'm sorry about that you are faild to upload image."
				,"img_key":"empty"
				,"img_url":"empty"
				})
			self.write(result)
		finally:
			self.finish()