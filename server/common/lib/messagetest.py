 #!/usr/bin/env python
 # coding=utf-8
# messagetest.py
#Author ChenXionghui
           
import sys
import os
reload(sys)   
sys.setdefaultencoding('utf8')  
location = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir)))+'/'
sys.path.append(location)
import time
import string
import pdb
import torndb
import modules.message
from common.variables import redis_dict
from common.lib.message import Message

db = torndb.Connection(
            host = '127.0.0.1', database = 'alumnuscircle',
            user = 'root', password = 'zp19950310'
        )
message = Message(db)
#redis_dict.flushall()
#print message.deal_message_to_one(1,"{test}",1)
#message.add_new_message_queue(4)
#print redis_dict.hgetall("circle:57c3ea9ab9a9964bf8c59e40")
print redis_dict.keys()
#if message.update_check(1,"circle:",'2016-08-28 20:57:41'):
#    print message.send_message(1)
print redis_dict.hgetall('user:5')
mid = message.create_message(type_id=1,circle_name='i apply a circle',circle_id='999')
message.deal_message_to_one(mid=mid,uid=14)
print redis_dict.hgetall('user:14')
#print redis_dict.hgetall('user:5')
#user_list='_5_6_7_8_'
#mid = message.create_message(type_id=1,circle_name='group message.',circle_id='999')
#message.deal_message_to_many(mid=mid,uid_list=user_list)
mid = message.create_message(type_id=1,circle_name='circle message.',circle_id='999')
print "circle list: " + str(redis_dict.hgetall('circle:14'))
message.deal_message_to_all(mid=mid,cid=14)
last_update_time='2016-08-31 17:57:06'
my_circle_list = '_10_11_12_14_15_'
print "circle:15"+str(redis_dict.hgetall('circle:15'))
print message.check_and_get_message(uid=14,my_circle_list=my_circle_list,last_update_time=last_update_time)
message.return_message_check(code=0,uid=14,my_circle_list=my_circle_list,last_update_time=last_update_time)
