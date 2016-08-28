 #!/usr/bin/env python
 # coding=utf-8
 # message.py

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


class CircleMessageModule(BaseModule):
    def __init__(self,db):
        BaseModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._manual_review_table =self.prefix+'manual_review_table'

        self._review_id = config.get(self._manual_review_table,"review_id")
        self._circle_name = config.get(self._manual_review_table,"circle_name")
        self._circle_icon_url = config.get(self._manual_review_table,"circle_icon_url")
        self._creator_uid = config.get(self._manual_review_table,"creator_uid")
        self._circle_type_id = config.get(self._manual_review_table,"circle_type_id")
        self._reason_message = config.get(self._manual_review_table,"reason_message")
        self._result = config.get(self._manual_review_table,"result")
        self._description = config.get(self._manual_review_table,"description")