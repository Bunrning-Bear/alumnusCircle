#!/usr/bin/env python
# coding=utf-8
# user.py
import json
import re
import ConfigParser

class UserHandler(object):
    _regex_dict2 = {} 
    def __init__(self):
        # ref: http://blog.jobbole.com/96052/
        # phone number begin with 13 or 14 or 15 or 17 or 18, 
        # length allowed is: 11.

        self._regex_dict2['phone_id'] = ur"^13[\d]{9}$|^14[5,7]{1}\d{8}$|^15[^4]{1}\d{8}$|^17[0,6,7,8]{1}\d{8}$|^18[\d]{9}$\Z"
        # begin with letter, length between 6 and 18, all allowed char are letter, number and underline.
        # length allowed is: 6 to 18
        self._regex_dict2['passwd'] = ur"^[a-zA-Z]\w{5,17}$\Z"
        # username should been decode with 'utf8',all allowed are chinese char, letter, number and underline.
        # length allowed is: 6 to 16
        self._regex_dict2['username'] = ur"^[\u4e00-\u9fa5\w]{1,15}$\Z"
        # the smallest qq id is 10000
        self._regex_dict2['qq_id'] = ur"[1-9][0-9]{4,}\Z"
        # wechat id can be letter, number and underline
        self._regex_dict2['wechat'] = ur"^[\w]{5,}$\Z"

class RegisterHandler(UserHandler):
    def __get_cryptedData(self,Data):
        # now, get access_token from umeng.
        return 1

if __name__ == '__main__':
    a = UserHandler()