 #!/usr/bin/env python
 # coding=utf-8
 # message.py
import logging
import ConfigParser

from base import BaseModule
from common.variables import AP
from base import BaseModule

class MessageModule(BaseModule):
    def __init__(self,db):
        BaseModule.__init__(self,db)
        self.prefix = self.prefix + 'message_'
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))


class CircleMessageModule(MessageModule):
    def __init__(self,db):
        MessageModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._circle_table =self.prefix+'circle_table'
        self._mc_id = config.get(self._circle_table,"mc_id")
        self._umeng_circle_id = config.get()


class UserMessageModule(MessageModule):
    def __init__(self,db):
        MessageModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._user_message_table = self.prefix+'user_table'
        self._uid = config.get(self._user_message_table,"uid")
        self.um_id = config.get(self._user_message_table,"mu_id")
        self.message_queue = config.get(self._user_message_table,"message_queue")
        self.update_time = config.get(self._user_message_table,"update_time")

    def set_user_to_message(self,uid):
        logging.info("query = %s"%("INSERT INTO " + self._user_message_table + "( " + self._uid + " ) " + "VALUES ( "+ str(uid)+")"))
        logging.info("in set user_ to message uid is %s"%uid)
        um_id = self.db.execute("INSERT INTO " + self._user_message_table + "( " + self._uid + " ) " + "VALUES ( %s )",uid)
        return um_id
    def get_update_time_by_uid(self,uid):
        update_time = self.db.get("SELECT update_time FROM " + self._user_message_table + " WHERE " + self._uid + "= %s", uid)
        return update_time