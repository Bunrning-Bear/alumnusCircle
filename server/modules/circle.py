#!usr/bin/env python
# coding=utf-8
# circle.py
import ConfigParser
from base import BaseModule
from common.variables import AP

class CircleModule(BaseModule):
    def __init__(self,db):
        BaseModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._circle_table =self.prefix+'circle_table'
        self._c_id = config.get(self._circle_table,"c_id")
        self._umeng_cid = config.get(self._circle_table,"umeng_cid")
        self._umeng_virtual_cid = config.get(self._circle_table,"umeng_virtual_cid")
        self._circle_type_id = config.get(self._circle_table,"circle_type_id")

    def set_circle_info(self,umeng_cid,umeng_virtual_cid,circle_type_id):
        """set several id of a circle in our app.
        those information will not been changed.
        """
        c_id = self.db.insert("INSERT INTO " + self._circle_table + "( " + self._umeng_cid +" , "+
            self._umeng_virtual_cid + " , " + self._circle_type_id 
            + " ) " + "VALUES (%s,%s,%s)",
            umeng_cid,umeng_virtual_cid,circle_type_id)
        return c_id

    def get_circle_umeng_cid(self,cid):
        umeng_cid = self.db.get(
            "SELECT "+ self._umeng_cid +
            " FROM " + self._circle_table + 
            " WHERE "+ self._c_id + " = %s LIMIT 1"
            ,cid)
        return umeng_cid[self._umeng_cid]