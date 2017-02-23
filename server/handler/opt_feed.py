#!usr/bin/env python
# coding=utf-8
# opt_feed.py
# Author ChenXionghui
"""
opt_feed define all of operate to feed:
include 
    comment, delete comment;
    like delete like;
    forward delete forawrd;
    [needn't] favourites delete favourites;
    get detail of a special feed;
    get commentlist of a special list;
"""
import json
import logging

import tornado.httpclient
import tornado.web
from request import RequestHandler
import base
import request
"""
pub my comment to a feed.
"""


class PubCommentHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(PubCommentHandler, self).__init__(*argc, **argkw)
        self.url = '/0/comment/pub'
        self.methodUsed = 'POST'
        self.requestName = 'pubComment'

    @request.authenticated('pubcomment')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        """
        request from client: 
            POST['info_json']:
                content:[must] content of comments
                img_str:[not need] url of image, splite by url.
                feed_id:[must] feed id
                reply_id:[not need] reply to other comment
                reply_uid:[not need] reply to other user
                image_urls?????
        """
        DataJson = self.get_argument('info_json')
        Data = json.loads(DataJson)
        uid = self.get_secure_cookie('uid')
        access_token = self.get_redis_dict_access_token(uid)
        count, message, Data = yield self.Umeng_asyn_request(access_token, Data)
        code = self.return_code_process(count)
        self.return_to_client(code, message, Data)

"""
delete a comment by pub user or feed creator.
[todo]:can Umeng check the comment deleted come from the creator of puber?
"""


class DeleteCommentHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(DeleteCommentHandler, self).__init__(*argc, **argkw)
        self.url = '/0/comment'
        self.methodUsed = 'DELETE'
        self.requestName = 'deleteComment'

    @request.authenticated('deleteComment')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @request.throwBaseException
    def post(self):
        """
        request from client: 
            POST['info_json']:
                comment_id[string]: [must] the comment client want to delete.
                [todo]: needn't check the id and the creator?
        """
        DataJson = self.get_argument('info_json')
        Data = json.loads(DataJson)

        access_token = self.get_redis_dict_access_token(uid)
        count, message, Data = yield self.Umeng_asyn_request(access_token, Data)
        code = self.return_code_process(count)
        #code,message = self.umeng_Api(self.url,self._public_access,Data,0,self.methodUsed)
        self.return_to_client(code, message, Data)


"""
this handler is to excute like feed, like comment, cancel like feed and cancel like comment.
"""


class LikeHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(LikeHandler, self).__init__(*argc, **argkw)
        self.url = '/0/like/feed'
        self.requestName = 'like'

    @request.authenticated('like')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
        Request from client: 
            POST['target']:[string] what you want to "like" can be feed or comment.
            POST['method']:[string] can be POST or DELETE.
                    notes:POST AND DELETE  must be upper letter.
            POST['info_json']:
                "feed_id":[string][must] the feed client like or want to cancel like.
        """
        uid = self.get_secure_cookie('uid')
        # self.url = self.url + self.get_argument('target')
        self.methodUsed = self.get_argument('method')
        feed_id = self.get_argument('feed_id')
        Data = {'feed_id': feed_id}
        access_token = self.get_redis_dict_access_token(uid)
        count, message, Data = yield self.Umeng_asyn_request(access_token, Data)
        code = self.return_code_process(count)
        #code,message = self.umeng_Api(self.url,self._public_access,Data,0,self.methodUsed)
        self.return_to_client(code, message, Data)

# [toodo] can not be used now!!!


"""
Get the detail of a sepcial feed.

"""


class FeedDetailHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(FeedDetailHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/show'
        self.methodUsed = 'GET'
        self.count = 10
        self.requestName = 'showfeed'

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
        Request from client:
            GET['page']:[integer][must]represent the page will return the next request.
            GET['feed_id']:[string][must] reprsent the detail of a special feed
        {
            "total": 1,
            "results": [
                {
                    "liked": "False",
                    "seq": 5756205,
                    "creator": {
                        "icon_url": "http://alumnuscircle.oss-cn-shanghai.aliyuncs.com/319791473743423.0.jpg?OSSAccessKeyId=LTAIkY3jD1E5hu8z&Expires=1487824536&Signature=kHRziMfICCt18Ko%2Bajk6jK728Bw%3D",
                        "medal_ids": [],
                        "id": "57d78a4ab9a9963fa44b2b3a",
                        "source_uid": "15851856958",
                        "name": "15851856958白洋"
                    },
                    "topics": [
                        {
                            "stats": "empty",
                            "description": "我们是有理想的IT精英",
                            "icon_url": "http://alumnuscircle.oss-cn-shanghai.aliyuncs.com/4327821473747285.5.jpg?OSSAccessKeyId=LTAIkY3jD1E5hu8z&Expires=1487824536&Signature=Z9rL3d4s7rzFUwBAi2blU8wePjo%3D",
                            "image_urls": [],
                            "custom": {
                                "virtual_cid": "57d79ab1b9a9964d13fd96ef",
                                "creator_uid": "118",
                                "creator_name": "陈小熊"
                            },
                            "id": "57d79ab1d36ef3cdf599bd89",
                            "name": "互联网创业圈"
                        }
                    ],
                    "tag": 0,
                    "readable_create_time": "01-18",
                    "id": "587f6bc7b9a9967cc4c35443",
                    "stats": {
                        "liked": 0,
                        "forwards": 0,
                        "comments": 1
                    },
                    "title": "沉雄辉bsb",
                    "origin_feed": "empty",
                    "custom": "",
                    "content": "萝莉控",
                    "source": "社区",
                    "location": {},
                    "media_type": 0,
                    "type": 0,
                    "rich_text": "",
                    "status": 0,
                    "is_topic_top": "empty",
                    "image_urls": [
                        "http://alumnuscircle.oss-cn-shanghai.aliyuncs.com/8851171484745633.04.jpg?OSSAccessKeyId=LTAIkY3jD1E5hu8z&Expires=1487824536&Signature=ydv3mGiUW3%2F4ZWa6yqID5V6mL3E%3D",
                        "http://alumnuscircle.oss-cn-shanghai.aliyuncs.com/279761484745660.58.jpg?OSSAccessKeyId=LTAIkY3jD1E5hu8z&Expires=1487824536&Signature=DpnjLgo3HNWeYF1lm72%2BDWlHPpE%3D"
                    ],
                    "is_top": 0,
                    "topic_tag": "",
                    "related_users": "empty",
                    "has_collected": "False",
                    "create_time": "2017-01-18 21:21:11",
                    "parent_feed_id": "",
                    "is_recommended": "True",
                    "share_link": "http://wsq.umeng.com/feeds/587f6bc7b9a9967cc4c35443/"
                }
            ]
        }
        """
        # page = self.get_argument('page')
        feed_id = self.get_argument('feed_id')
        # Data = {'page':page,'count':self.count,'feed_id':feed_id}
        Data = {'feed_id': feed_id}
        access_token = self._public_access
        count, message, Data = yield self.public_Umeng_request(Data)
        result = self.deleted_useless_feed(Data['results'][0])
        code = self.return_code_process(count)
        self.return_to_client(code, message, result)
        self.finish()


"""
Get comment list of a special feed
"""

class CommentListHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(CommentListHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/comments'
        self.methodUsed = 'GET'
        self.order = "seq"  # result order
        self.requestName = 'commentlist'

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
        Args：
            GET['page']:[integer][must]represent the page will return the next request.
            GET['feed_id']:[string][must] reprsent the detail of a special feed

        Returns:
        "response": {
            "count": 30,
            "total": 6,
            "page": 1,
            "results": [
                {
                    "status": 0,＃　不要
                    "reply_user": "empty",# 不要
                    "liked": false,
                    "stats": { # 不要
                        "liked": 0
                    },
                    "floor": 2,
                    "creator": { 
                        "icon_url": "http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg",　＃　不要
                        "medal_ids": "empty",#不要
                        "id": "57d2c60fd36ef3ede3236ebb",
                        "source_uid": "15888888888",＃不要
                        "name": "15888888888大神"
                    },
                    "image_urls": "empty",＃不要
                    "content": "我评论了这条动态! 我评论了这条动态",
                    "source": "社区",＃不要
                    "create_time": "2016-09-10 00:35:39",＃不要
                    "readable_create_time": "00:35",＃不要
                    "reply_comment": "empty",＃不要
                    "id": "57d2e4dbb9a9964d13fd6db8",＃不要
                    "feed": {＃　不要
                        "status": 0,
                        "creator": {
                            "icon_url": "http://b.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=45f10be75edf8db1bc7b74603c13f162/023b5bb5c9ea15ce2f42ea76b6003af33a87b224.jpg",
                            "medal_ids": "empty",
                            "id": "57d2c60fd36ef3ede3236ebb",
                            "source_uid": "15888888888",
                            "name": "15888888888大神"
                        },
                        "image_urls": [
                            "http://tupian.qqjay.com/tou3/2016/0605/9848ad4d58f2cf2ac07a2645d66e20e6.jpg",
                            "http://tupian.qqjay.com/tou3/2016/0605/222393536f052f6d5c1e293b8e065164.jpg"
                        ],
                        "content": "这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!这是一条很长的中文动态,里面有很长的内容, 大神在里面评论了好多东西!!!!!",
                        "create_time": "2016-09-10 00:33:17",
                        "readable_create_time": "00:33",
                        "id": "57d2e44dd36ef3fbfcb032e4"
                    }
                },

        """

        page = self.get_argument('page')
        feed_id = self.get_argument('feed_id')
        count = self.get_argument('count')
        Data = {'page': page, 'count': self.count,
                'feed_id': feed_id, "count": count}
        access_token = self._public_access
        count, message, umengData = yield self.public_Umeng_request(Data)
        for dictUnit in umengData['results']:
            del dictUnit['status']
            del dictUnit['reply_user']
            del dictUnit['stats']
            del dictUnit['creator']['icon_url']
            del dictUnit['creator']['medal_ids']
            del dictUnit['creator']['source_uid']
            del dictUnit['image_urls']
            del dictUnit['create_time']
            dictUnit['feed'] = dictUnit['feed']['id']
            del dictUnit['readable_create_time']
            del dictUnit['reply_comment']
            del dictUnit['id']
            del dictUnit['floor']
            del dictUnit['source']
        code = self.return_code_process(count)
        self.return_to_client(code, message, umengData)
        self.finish()

"""
[needn't now] 
this handler is to forwoard a feed.
"""


class ForwoardHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(ForwoardHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/forward'
        self.requestName = 'forward'
        self.methodUsed = 'POST'
        self.requestName = 'forward'

    @request.authenticated('forward')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
            request from client: 
                POST['info_json']:
                    "topic_ids":[string][needn't] topic id, splite by ,
                    "content":[string][needn't] feed content
                    "feed_id":[string][must] forward feed id
                    "related_id":[string][needn't] related user splete by ,
                    etc: location,lat,lng.
        """
        uid = self.get_secure_cookie('uid')
        DataJson = self.get_argument('info_json')
        Data = json.loads(DataJson)
        access_token = self.get_redis_dict_access_token(uid)
        code, message, Data = yield self.Umeng_asyn_request(access_token, Data)

        self.return_to_client(code, message, Data)

"""
[needn't]
This handler is to favourite a feed or cancel a favourited feed. 
"""


class FavouritesHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(FavouritesHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/favourites/'
        self.requestName = 'favourites'
        self.methodUsed = 'POST'

    @request.authenticated('favourites')
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        uid = self.get_secure_cookie('uid')
        """
        Request from client:
            POST['target']:[string]can be destory or create,must be lowwer letter.
                    destory: means cancel a favourited feed.
                    create: means favourite feed.
            POST['info_json']:
                   "feed_id":[string][must] forward feed id     
        """
        self.url = self.url + self.get_argument('target')
        DataJson = self.get_argument('info_json')
        Data = json.loads(DataJson)
        access_token = self.get_user_dict(uid)[1]
        code, message, Data = yield self.Umeng_asyn_request(access_token, Data)
        self.return_to_client(code, message, Data)
