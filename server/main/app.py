# app.py
import sys
reload(sys)   
sys.setdefaultencoding('utf8')  
location = '/home/burningbear/CodePlace/python/web/alumnusCircle/server/'
sys.path.append(location)

import ConfigParser
import logging
import MySQLdb
import torndb
import tornado.httpserver
import tornado.ioloop 
import tornado.options
import tornado.web

import handler.index
import handler.user
import handler.my_feed
import handler.feed_list
import handler.user_list
import handler.opt_feed
import handler.opt_user
import handler.topic

from common.variables import AP 
from tornado.options import define, options
define("port", default = 8000, help = "run on the given port", type = int)
define("mysql_host", default = "127.0.0.1", help = "community database host")
define("mysql_database", default = "alumnuscircle", help = "community database name")
define("mysql_user", default = "root", help = "community database user")
define("mysql_password", default = "zp19950310", help = "community database password")

logging.basicConfig(level=logging.INFO)
#                    filename='err.log',  
#                   filemode='w')

class Application(tornado.web.Application):
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+"common/conf.ini"))
        cookie_secret = config.get("app","cookie_secret")
        self._user_dict = {}
        settings = dict(
            cookie_secret=cookie_secret,
            xsrf_cookies=True
        )
        handlers = [
        (r'/',handler.index.IndexHandler),
        (r'/register',handler.user.RegisterHandler),
        (r'/login',handler.user.LoginHandler),
        (r'/logout',handler.user.LogoutHandler),
        (r'/updateinfo',handler.user.UpdataInfoHandler),
        (r'/uploadfile',handler.base.UploadFileHandler),

        (r'/follow',handler.opt_user.FollowHandler),
        (r'/searchuser',handler.opt_user.SearchUserHandler),

        (r'/followslist',handler.user_list.FollowsListHandler),

        (r'/myfeed/update',handler.my_feed.UpdateFeedHandler),
        (r'/myfeed/delete',handler.my_feed.DeleteFeedHandler),
        (r'/timefeedList',handler.feed_list.TimelineHandler),
        (r'/myfavouritelist',handler.user_list.FavouriteslistHandler),

        (r'/createtopic',handler.topic.CeateTopicHandler),
        (r'/detailtopic',handler.topic.DetailTopicHandler),

        (r'/pubcomment',handler.opt_feed.PubCommentHandler),
        (r'/deletecomment',handler.opt_feed.DeleteCommentHandler),
        (r'/like',handler.opt_feed.LikeHandler),
        (r'/forward',handler.opt_feed.ForwoardHandler),
        (r'/favourite',handler.opt_feed.FavouritesHandler),
        (r'/detail',handler.opt_feed.DetailHandler),
        (r'/commentlist',handler.opt_feed.CommentListHandler)
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        # add db to global variable.
        self.db = torndb.Connection(
            host = options.mysql_host, database = options.mysql_database,
            user = options.mysql_user, password = options.mysql_password
        )
        """
        TODO:[xionghui]2016.8.2,complete database error
        try:
            a = self.db.get("SELECT COUNT(*) from user_info")
        except MySQLdb.ProgrammingError:
        """

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()