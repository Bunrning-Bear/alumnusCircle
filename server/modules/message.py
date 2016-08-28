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
        self._circle_table =self.prefix+'circle_table'
        self._mc_id = config.get(self._circle_table,"mc_id")
        self._umeng_circle_id = config
[ac_message_circle_table]
mc_id=mc_id
umeng_circle_id
queue_list=queue_list