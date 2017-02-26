#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author Zhengfan
# Date 16.09.06
# Version 1.0
# Include ImageCache ExecuteSQL Aliyun

import os
import base64

import oss2


# Author Zhengfan
# Date 16.09.06
# Version 1.0
# Function Save images from client to local disk.
# Note Be used in Upload * Handler
class ImageCache(object):
    def __init__(self, *arg, **argkw):
        super(ImageCache, self).__init__(*arg, **argkw)

    def saveBase64ImgStr(self, localCacheAbsolutePath, base64ImgStr):
        if(localCacheAbsolutePath == None or base64ImgStr == None):
            raise
        imgFile = base64.b64decode(base64ImgStr)
        with open(localCacheAbsolutePath, 'wb') as cache:
            cache.write(imgFile)
        return True

    def saveImgBytes(self, localCacheAbsolutePath, imgBytes):
        with open(localCacheAbsolutePath, 'wb') as cache:
            cache.write(imgBytes)
        return True

    def removeImgFile(self, localCacheAbsolutePath):
        if not os.path.exists(localCacheAbsolutePath):
            raise
        os.remove(localCacheAbsolutePath)
        return True


# Author Zhengfan
# Date 16.09.06
# Version 1.0
# Function Encapsulates all of funtions about MySQL Database.
# Note Be used in Upload * Handler
class ExecuteSQL(object):
    def __init__(self, *arg, **argkw):
        super(ExecuteSQL, self).__init__(*arg, **argkw)

    def update_user_detail_info(self, db, key, uid):
        TABLE_NAME = "ac_user_detail_info"
        COLUMN_NAME = "icon_url"
        CONDITION = "WHERE uid = " + "'" + uid + "'"
        rawSQL = "UPDATE" + " " + TABLE_NAME + " " + "SET" + " " + \
            COLUMN_NAME + " " + "=" + "  '" + key + "' " + CONDITION
        db.execute(rawSQL)

    def update_user_list_info(self, db, key, uid):
        TABLE_NAME = "ac_user_list_info"
        COLUMN_NAME = "icon_url"
        CONDITION = "WHERE uid = " + "'" + uid + "'"
        rawSQL = "UPDATE" + " " + TABLE_NAME + " " + "SET" + " " + \
            COLUMN_NAME + " " + "=" + "  '" + key + "' " + CONDITION
        db.execute(rawSQL)

    def update_circle_table(self, db, key, cid):
        TABLE_NAME = "ac_circle_table"
        COLUMN_NAME = "icon_url"
        CONDITION = "WHERE cid = " + "'" + cid + "'"
        rawSQL = "UPDATE" + " " + TABLE_NAME + " " + "SET" + " " + \
            COLUMN_NAME + " " + "=" + "  '" + key + "' " + CONDITION
        db.execute(rawSQL)


# Author Zhengfan
# Date 16.09.06
# Version 1.0
# Function Encapsulates all of funtions about the aliyun cloud services.
# Note Be used in lots of outside modules
class Aliyun(object):
    def __init__(self, *arg, **argkw):
        super(Aliyun, self).__init__(*arg, **argkw)
        self.auth = oss2.Auth('LTAIkY3jD1E5hu8z',
                              '9zgLrLOjr9ebRFoI3OV5qDE7BKqIhU')
        self.endpoint = r'http://oss-cn-shanghai.aliyuncs.com'
        self.bucketName = 'alumnuscircle'
        self.service = oss2.Service(self.auth, self.endpoint)
        self.bucket = oss2.Bucket(self.auth, self.endpoint, self.bucketName)

    def uploadImgFile(self, key, localCacheAbsolutePath):
        result = self.bucket.put_object_from_file(key, localCacheAbsolutePath)
        if(result.status != 200):
            raise
        return True

    def uploadImgBytes(self, key, imgBytes):
        result = self.bucket.put_object(key, imgBytes)
        if(result.status != 200):
            raise
        return True

    def downloadImgFile(self, key, localCacheAbsolutePath):
        bucket.get_object_to_file(key, localCacheAbsolutePath)
        if not os.path.exists(localCacheAbsolutePath):
            raise
        return True

    def parseUrlByKey(self, key):
        return self.bucket.sign_url('GET', key, 300)

    def parseUrlByFakeKey(self, fakeKey):

        # logging.info("---------------------------------------------fackkey is %s"%fackkey)

        # logging.info("fackkey is %s"%fackkey)
        keyPrefix = r'http://www.seu.edu.cn/'
        asciiKeyPrefix = r'http%3A%2F%2Fwww.seu.edu.cn%2F'
        if(keyPrefix in fakeKey):
            key = fakeKey[22:]
            return self.parseUrlByKey(key)
        elif(asciiKeyPrefix in fakeKey):
            key = fakeKey[30:]
            return self.parseUrlByKey(key)
        else:
            return fakeKey
