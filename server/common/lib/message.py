#!usr/bin/env python
# coding=utf-8
# message.py
import modules.message
from common.variables import user_dict, circle_dict
class Message(object):
    def __init__(self,db):
        self._user_message = modules.message.UserMessageModule(db)
        

    @property
    def user_message(self):
        return self._user_message
    
    def init_message(self,uid):
        update_time = self.user_message.get_update_time_by_uid(uid)
        return update_time
