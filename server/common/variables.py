#!/usr/bin/env python
import redis
import logging
import os
redis_dict = redis.Redis(host='localhost',port=6379)
AP = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))+'/'
CODE_DICT = {
    # server part
    "database": 1100,
    "cookie": 1120,
    # user part
    "register": 1200,
    "login": 1200,
    "logout":1300,
    "checkphone":3000,

    "update":1400,
    "delete":1450,
    "pubComment":1500,
    "deleteComment":1600,
    "like":1700,
    "favourite":1900,
    "follow":2000,
    "searchuser":2100,
    "showfeed":2200,
    "followsList":2300,
    "topic":2400,
    "topicdetail":2500,
    "userdetail":2600,
    "update_user_info":2700,
    "create_topic":2800,
    "review_topic":2900,

    'receive_apply':3100,
    "get_all_topic":3200,
    "circle_feed":3300,
    "user_filter":3400,
    "circle_member":3500,
    "sendmessage":3600,
    "get_comment":3700,
    "check_message":3800,
    "circle_apply":3900,
    "user_topic":4000,
    "commentlist":4100,
    "topictype":4200,
    "get_comment_list":4300
}