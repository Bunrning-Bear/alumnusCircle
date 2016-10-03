#!/usr/bin/python
# -*- coding: utf-8 -*-
# login.py
# urllibtest.py
# coding=utf-8
"""
Header_name     Header_value    Description
Accept  application/json    服务器端返回给客户端的数据类型
Content-Type    application/json    客户端发送到服务器端的数据类型

"""
import urllib2
import urllib
import cookielib
import json
import random
import hashlib
prefix = 'https://a1.easemob.com/alumnuscircle/alumnuscircle/'
#prefix = "https://a1.easemob.com/alumnuscircle/alumnuscircle/"
# prefix = "http://127.0.0.1:8003"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

url = prefix + 'token'
headers = {'Content-Type': 'application/json'}
"""
data = {'grant_type': 'client_credentials',
        'client_id': 'YXA6wDs-MARqEeSO0VcBzaqg11',
        'client_secret': 'YXA6JOMWlLap_YbI_ucz77j-4-mI0dd'}
"""

data = {'grant_type': 'client_credentials',
        'client_id': 'YXA6HmI74IbREeaQ0-99kUW07Q',
        'client_secret': 'YXA67T22sKInjwTTVuO3nS7j5gf87eE'}
data = json.dumps(data)

# data = urllib.urlencode(data)
request = urllib2.Request(url, data, headers)
request.get_method = lambda: 'POST'  # or 'DELETE'
try:
    response = urllib2.urlopen(request)
except Exception, e:
    print e.read()
else:
    pass
finally:
    pass
the_page = response.read()
dictresult = eval(the_page)
access_token = dictresult['access_token']


# send message.


# url = prefix + 'messages'
# headers = {'Content-Type': 'application/json',
#            'Authorization': 'Bearer ' + access_token}
# data = {
#     'target_type': 'users',
#     'target': ['15195861109'],
#     'msg': {
#         'type': 'txt',
#         'msg': 'hello from test2'
#     },
#     'from': 'EXGY93'
# }
# data = json.dumps(data)
# request = urllib2.Request(url, data, headers)
# try:
#     response = urllib2.urlopen(request)
# except Exception, e:
#     print e.read()
# else:
#     pass
# finally:
#     pass
# the_page = response.read()
# print the_page


# get my offline message number .

# url = prefix + 'users/' + '15195861109' + '/offline_msg_count'
# print url
# headers = {'Authorization': 'Bearer ' + access_token}
# print headers
# request = urllib2.Request(url, headers=headers)
# request.get_method = lambda: 'GET'
# try:
#     response = urllib2.urlopen(request)
# except Exception, e:
#     print e.read()
# else:
#     pass
# finally:
#     pass
# the_page = response.read()
# print the_page


"""
this is register method demo

url = prefix + 'users'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + access_token}
data = {'username': '15195861109', 'password': '123456'}
data = json.dumps(data)
request = urllib2.Request(url, data, headers)
try:
    response = urllib2.urlopen(request)
except Exception, e:
    print e.read()
else:
    pass
finally:
    pass
the_page = response.read()
"""

"""
resp = urllib2.urlopen(prefix + '/')
the_page = resp.read()
print resp.getcode() == 200
print the_page

_xsrf = json.loads(the_page)['Data']['_xsrf']


def set_resquest(api, data, method):
    # data is dictory.
    # method can be get put delete post ?
    # get _xsrff
    for item in cj:
        if item.name == '_xsrf':
            _xsrf = item.value
    if method != 'GET':
        data['_xsrf'] = _xsrf
    data = urllib.urlencode(data)
    url = prefix + api
    if method == 'GET':
        url = url + "?" + data
    request = urllib2.Request(url, data)
    request.get_method = lambda: method  # or 'DELETE'
    return request


def setMessage(message, num, content):
   message[num] = "No.%s " % num + content + "\r\n"


def set_info_json(dic):
    info_json = json.dumps


def do_request(api, dic, message, method, otherPara):
    count = 0
    while count < len(dic):
        info_json = json.dumps(dic[count])
        para = otherPara[count]
        para['info_json'] = info_json
        # print "do request :" + str(para) + str(ot)
        req = set_resquest(api, para, method)
        response = urllib2.urlopen(req)
        the_page = response.read()
        print message[count] + the_page
        count = count + 1
"""
