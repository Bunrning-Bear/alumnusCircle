# app.py
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
import handler.topic
from handler.web.login import IndexWebHandler
from common.variables import AP 
from common.variables import redis_dict
from tornado.options import define, options
from common.lib.message import Message

define("port", default = 8000, help = "run on the given port", type = int)
define("mysql_host", default = "127.0.0.1", help = "community database host")
define("mysql_database", default = "alumnuscircle", help = "community database name")
define("mysql_user", default = "root", help = "community database user")
define("mysql_password", default = "zp19950310", help = "community database password")

logging.basicConfig(level=logging.INFO)
              #  filename='err.log',  
              #  filemode='w')

class Application(tornado.web.Application):
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+"common/conf.ini"))
        cookie_secret = config.get("app","cookie_secret")
        self._redis_dict = redis_dict
        logging.info("start server.")
        settings = dict(
            cookie_secret=cookie_secret,
            xsrf_cookies=True
        )
        template_path=os.path.join(os.path.dirname(__file__), "templates")
        handlers = [
        # web
        (r'/adminlogin',IndexWebHandler),
        # user
        (r'/adminregister',handler.user.RegisterAdminHandler),
        (r'/',handler.index.IndexHandler),
        (r'/checkphone',handler.user.CheckTelephoneHandler),
        (r'/register',handler.user.RegisterHandler),
        (r'/login',handler.user.LoginHandler),
        (r'/logout',handler.user.LogoutHandler),
        (r'/updateinfo',handler.user.UpdataInfoHandler),
        (r'/uploadfile',handler.base.UploadFileHandler),
        # user-user
        (r'/follow',handler.opt_user.FollowHandler),
        (r'/searchuser',handler.opt_user.SearchUserHandler),

        (r'/followslist',handler.user_list.FollowsListHandler),
        # feed
        (r'/myfeed/update',handler.my_feed.UpdateFeedHandler),
        (r'/myfeed/delete',handler.my_feed.DeleteFeedHandler),
        (r'/timefeedList',handler.feed_list.TimelineHandler),
        (r'/myfavouritelist',handler.user_list.FavouriteslistHandler),
        # circle
        (r'/circle_apply_result',handler.topic.ReceiveApplyReviewHandler),
        (r'/get_my_filter_circle',handler.topic.GetMyfilterCircleHander),
        (r'/get_my_circle',handler.topic.GetMyCircleHandler),
        (r'/createTopic',handler.topic.CeateTopicHandler),
        (r'/detailtopic',handler.topic.DetailTopicHandler),
        (r'/edittopic',handler.topic.EditTopicHandler),
        (r'/gettypetopic',handler.topic.GetTopicTypeHandler),
        (r'/searchtopic',handler.topic.SearchTopicHandler),

        (r'/reviewlisttopic',handler.topic.ReviewListHandler),
        (r'/reviewresult',handler.topic.ReviewResultHandler),

        (r'/pubcomment',handler.opt_feed.PubCommentHandler),
        (r'/deletecomment',handler.opt_feed.DeleteCommentHandler),
        (r'/like',handler.opt_feed.LikeHandler),
        (r'/forward',handler.opt_feed.ForwoardHandler),
        (r'/favourite',handler.opt_feed.FavouritesHandler),
        (r'/detail',handler.opt_feed.DetailHandler),
        (r'/commentlist',handler.opt_feed.CommentListHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        # add db to global variable.
        self.db = torndb.Connection(
            host = options.mysql_host, database = options.mysql_database,
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
        self.es = Elasticsearch([{'host':'localhost','port':9200}])

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()


"c54e996f6c839595aa41ab4a89052b7fc416c223"