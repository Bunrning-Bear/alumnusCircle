# app.py
#Author ChenXionghui
import sys
import os
reload(sys)   
sys.setdefaultencoding('utf8')  
location = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))+'/'
sys.path.append(location)

import ConfigParser
import logging
import MySQLdb
import torndb
import tornado.httpserver
import tornado.ioloop 
import tornado.options
import tornado.web
import redis
from elasticsearch import Elasticsearch
import handler.index
import handler.user
import handler.my_feed
import handler.feed_list
import handler.user_list
import handler.opt_feed
import handler.opt_user
import handler.circle.circle
import handler.circle.circle_detail
import handler.contact
import handler.message 
import handler.test
import handler.circle.opt_circle
import handler.upload_user_hdimg
import handler.upload_circle_hdimg
import handler.upload_feed_img
import handler.upload_normal_img

from handler.web.login import IndexWebHandler,MainWebHandler
from common.variables import AP 
from common.variables import redis_dict
from tornado.options import define, options
from common.lib.message import Message

define("port", default = 8000, help = "run on the given port", type = int)
define("host", default = "127.0.0.1", help = "community database host")
define("mysql_database", default = "alumnuscircle", help = "community database name")
define("mysql_user", default = "root", help = "community database user")
define("mysql_password", default = "zp19950310", help = "community database password")

logging.basicConfig(level=logging.INFO,
               filename='err.log',  
               filemode='w')

class Application(tornado.web.Application):
    def __init__(self, *argc, **argkw):
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+"common/conf.ini"))
        cookie_secret = config.get("app","cookie_secret")
        self._redis_dict = redis_dict
        # [test]
        self._redis_dict.flushall()

        template_path=os.path.join(AP+"template")
        static_path=os.path.join(AP+"static")
        logging.info("start server.")
        settings = dict(
            cookie_secret=cookie_secret,
            xsrf_cookies=True,
            template_path=template_path,
            static_path=static_path
        )

        handlers = [
        # test
        (r'/test', handler.test.TestHandler),
        # web
        (r'/adminlogin',IndexWebHandler),
        (r'/admin_main',MainWebHandler),
        (r'/admin_toreview',handler.circle.circle.ReviewListHandler),
#        (r'/admin_hasreview',HasReviewHandler),
        # user
        (r'/adminregister',handler.user.RegisterAdminHandler),
        (r'/',handler.index.IndexHandler),
        (r'/checkphone',handler.user.CheckTelephoneHandler),
        (r'/register',handler.user.RegisterHandler),
        (r'/login',handler.user.LoginHandler),
        (r'/logout',handler.user.LogoutHandler),
        (r'/updateinfo',handler.user.UpdataInfoHandler),    

        # user-user
        (r'/follow',handler.opt_user.FollowHandler),
        (r'/searchuser',handler.opt_user.SearchUserHandler),
        (r'/followslist',handler.user_list.FollowsListHandler),
        (r'/user_detail',handler.contact.UserDetailHandler),
        
        # my feed
        (r'/myfeed/update',handler.my_feed.UpdateFeedHandler),
        (r'/myfeed/delete',handler.my_feed.DeleteFeedHandler),
        
        # message
        (r'/getmessage',handler.message.GetMessageHandler),
        (r'/get_my_comment',handler.message.GetMyCommentHandler),
        (r'/checkmessage',handler.message.CheckMessageHandler),
        
        (r'/timefeedList',handler.feed_list.TimelineHandler),
        (r'/myfavouritelist',handler.user_list.FavouriteslistHandler),
        
        # feed detail:
        (r'/feed_detail',handler.opt_feed.FeedDetailHandler),
        (r'/pubcomment',handler.opt_feed.PubCommentHandler),
        (r'/like',handler.opt_feed.LikeHandler),
        (r'/commentlist',handler.opt_feed.CommentListHandler),
        # message :
        #  (r'/receive_message',handler.message.)
        #(r'/deletecomment',handler.opt_feed.DeleteCommentHandler),
        #(r'/forward',handler.opt_feed.ForwoardHandler),
        #(r'/favourite',handler.opt_feed.FavouritesHandler),
        
        # circle
        (r'/circle_apply_result',handler.circle.circle.ReceiveApplyReviewHandler),
        (r'/get_my_filter_circle',handler.circle.circle.GetMyfilterCircleHander),
        (r'/get_my_circle',handler.circle.circle.GetMyCircleHandler),
        (r'/circle_member_list',handler.circle.circle_detail.CircleMemberHandler),

        # circle _operation
        (r'/apply_circle',handler.circle.opt_circle.CircleApplyHandler),
        (r'/leave_circle',handler.circle.opt_circle.LeaveCircleHandler),
        # circle-detail
        (r'/detail_circle',handler.circle.circle_detail.DetailCircleHandler),
        (r'/circle_feed',handler.circle.circle_detail.CircleFeedListHandler),
        (r'/createTopic',handler.circle.circle.CeateTopicHandler),
        (r'/edittopic',handler.circle.circle.EditTopicHandler),
        (r'/gettypetopic',handler.circle.circle.GetTopicTypeHandler),
        (r'/searchtopic',handler.circle.circle.SearchTopicHandler),

        # search user
        (r'/search_user',handler.contact.UserFilterHandler),
        # review circle
        (r'/reviewlisttopic',handler.circle.circle.ReviewListHandler),
        (r'/reviewresult',handler.circle.circle.ReviewResultHandler),

        # upload image
        (r'/upload_user_hdimg',handler.upload_user_hdimg.UploadUserHdimgHandler),
        (r'/upload_circle_hdimg',handler.upload_circle_hdimg.UploadCircleHdimgHandler),
        (r'/upload_feed_img',handler.upload_feed_img.UploadFeedImgHandler),
        (r'/upload_normal_img',handler.upload_normal_img.UploadNormalImgHandler)


        ]
        tornado.web.Application.__init__(self, handlers,**settings)
        # add db to global variable.
        self.db = torndb.Connection(
            host = options.host, database = options.mysql_database,
            user = options.mysql_user, password = options.mysql_password
        )
        self.message = Message(self.db)
        self.message.init_message_to_all()
        """
        TODO:[xionghui]2016.8.2,complete database error
        try:
            a = self.db.get("SELECT COUNT(*) from user_info")
        except MySQLdb.ProgrammingError:
        """
        self.es = Elasticsearch([{'host':options.host,'port':9200}])

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

