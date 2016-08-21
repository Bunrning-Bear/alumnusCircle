# opt_feed.py
"""
opt_feed define all of operate to feed:
include 
comment, delete comment;
like delete like;
forward delete forawrd;
favourites delete favourites;
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
        access_token = self.get_user_dict(uid)[1]
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)
        self.return_to_client(code,message,Data)

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
    def post(self):
        """
        request from client: 
            POST['info_json']:
                comment_id[string]: [must] the comment client want to delete.
                [todo]: needn't check the id and the creator?
        """
        DataJson = self.get_argument('info_json')
        Data = json.loads(DataJson)

        access_token = self.get_user_dict(uid)[1]
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)       
        #code,message = self.umeng_Api(self.url,self._public_access,Data,0,self.methodUsed)
        self.return_to_client(code,message,Data)


"""
this handler is to excute like feed, like comment, cancel like feed and cancel like comment.
"""
class LikeHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(LikeHandler, self).__init__(*argc, **argkw)
        self.url = '/0/like/'
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
        self.url = self.url + self.get_argument('target')
        self.methodUsed = self.get_argument('method')
        DataJson = self.get_argument('info_json')
        Data = json.loads(DataJson)
        access_token = self.get_user_dict(uid)[1]
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)    
        #code,message = self.umeng_Api(self.url,self._public_access,Data,0,self.methodUsed)
        self.return_to_client(code,message,Data)

# [toodo] can not be used now!!!
"""
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
        access_token = self.get_user_dict(uid)[1]
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)    
        self.return_to_client(code,message,Data)    

"""
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
        code,message,Data =yield self.Umeng_asyn_request(access_token,Data)    
        self.return_to_client(code,message,Data)    


"""
Get the detail of a sepcial feed.

"""
class DetailHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(DetailHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/show'
        self.methodUsed = 'GET'
        self.count =10
        self.requestName = 'showfeed'
    
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        """
        Request from client:
            GET['page']:[integer][must]represent the page will return the next request.
            GET['feed_id']:[string][must] reprsent the detail of a special feed
        """
        page = self.get_argument('page')
        feed_id = self.get_argument('feed_id')
        Data = {'page':page,'count':self.count,'feed_id':feed_id}
        access_token = self._public_access
        code,message,Data = yield self.public_Umeng_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()


"""
Get comment list of a special feed
"""
class CommentListHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
        super(CommentListHandler, self).__init__(*argc, **argkw)
        self.url = '/0/feed/comments'
        self.methodUsed = 'GET'
        self.order = "seq"# result order  
        self.requestName = 'commentlist'
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        """
        Request from client:
            GET['page']:[integer][must]represent the page will return the next request.
            GET['feed_id']:[string][must] reprsent the detail of a special feed
        """
        page = self.get_argument('page')
        feed_id = self.get_argument('feed_id')
        Data = {'page':page,'count':self.count,'feed_id':feed_id}
        access_token = self._public_access
        code,message,Data = yield self.public_Umeng_request(access_token,Data)
        self.return_to_client(code,message,Data)
        self.finish()
