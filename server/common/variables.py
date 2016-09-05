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
    "check_phone":3000,
}