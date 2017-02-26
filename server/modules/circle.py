#!usr/bin/env python
# coding=utf-8
# circle.py
import ConfigParser
from base import BaseModule
from common.variables import AP
import logging


class CircleModule(BaseModule):
    def __init__(self, db):
        BaseModule.__init__(self, db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP + 'common/conf.ini'))
        self._circle_table = self.prefix + 'circle_table'
        self._c_id = config.get(self._circle_table, "c_id")
        self._umeng_cid = config.get(self._circle_table, "umeng_cid")
        self._umeng_virtual_cid = config.get(
            self._circle_table, "umeng_virtual_cid")
        # self._circle_type_id = config.get(self._circle_table,"circle_type_id")
        self._icon_url = config.get(self._circle_table, "icon_url")

    def set_circle_info(self, umeng_cid, umeng_virtual_cid, icon_url):
        """set several id of a circle in our app.
        those information will not been changed.
        """
        c_id = self.db.insert("INSERT INTO " + self._circle_table + "( " + self._umeng_cid + " , " +
                              self._umeng_virtual_cid + " , " + self._icon_url
                              + " ) " + "VALUES (%s,%s,%s)",
                              umeng_cid, umeng_virtual_cid, icon_url)
        return c_id

    def get_circle_umeng_cid(self, cid):
        umeng_cid = self.db.get(
            "SELECT " + self._umeng_cid +
            " FROM " + self._circle_table +
            " WHERE " + self._c_id + " = %s LIMIT 1", cid)
        return umeng_cid[self._umeng_cid]

    def get_cid_from_umeng_id(self, umeng_cid):
        cid = self.db.get(
            "SELECT " + self._c_id +
            " FROM " + self._circle_table +
            " WHERE " + self._umeng_cid + " = %s LIMIT 1", umeng_cid)
        return cid[self._c_id]

    def get_icon_url_from_cid(self, cid):
        icon_url = self.db.get(
            "SELECT " + self._icon_url +
            " FROM " + self._circle_table +
            " WHERE " + self._c_id + " = %s LIMIT 1", cid)
        return icon_url[self._icon_url]
