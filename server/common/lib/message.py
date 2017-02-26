#!usr/bin/env python
# coding=utf-8
# message.py
#Author ChenXionghui
import sys
import os
reload(sys)   
sys.setdefaultencoding('utf8')  
location = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir)))+'/'
sys.path.append(location)
import logging
import time
import string
import pdb
import torndb
import modules.message
from common.variables import redis_dict

"""Message class is to deal the process of a message.
"""
class Message(object):
    def __init__(self,db):
        self._user_message = modules.message.UserMessageModule(db)
        self._circle_message = modules.message.MessageCircleModule(db)
        self._message = modules.message.MessagesListModule(db)
        self.TYPE = {
            "create circle success":0,
            "create circle fail":1,
            "new member":2,
            "apply circle result":3,
            "apply circle":4
        }
        self.format_time = "%Y-%m-%d %H:%M:%S"
    @property
    def user_message(self):
        return self._user_message
    
    @property
    def circle_message(self):
        return self._circle_message
    
    @property
    def message(self):
        return self._message

    def create_message(
        self,type_id,circle_name=' ',circle_id=' ',reason=' ',circle_url='',uid='',result = '',username=''):
        """input parameter of a special type of message, then return the message id.

        Args:
            type_id: message type id, look "databases.md" for detail
            circle_name:
            circle_id:
            reason: 

        Returns:
            mid of ac_message_table.
        """
        if type_id == 0:
            # create circle successfully.
            dic = {
            'circle_name':circle_name,
            'circle_id':circle_id,
            "circle_url":circle_url}
        elif type_id == 1:
            # create circle failed.
            dic = {
            'circle_name':circle_name,
            "circle_url":circle_url}
        elif type_id == 2:
            # welcome to new member
            dic = {
            'circle_name':circle_name,# apply circle name.
            "circle_id":circle_id,# apply circle id.
            "circle_url":circle_url,# apply circle url.
            "apply_uid":uid,# apply user id.
            "apply_name":username,
            }
        elif type_id == 3:
            dic = {
            'circle_name':circle_name,# apply circle name.
            "circle_id":circle_id,# apply circle id.
            "circle_url":circle_url,# apply circle url.
            "result":result# apply result
            }
        elif type_id == 4:# apply to a circle, send to amin and creator
             dic = {
             "circle_id":circle_id,
             "circle_name":circle_name,
             "circle_url":circle_url,
             "reason":reason,
             "apply_uid":uid,
             "apply_name":username
             }
        mid = self.message.set_message(type_id,dic)
        return mid

    def init_message(self,uid):
        """After user login, we should store its update information in redis dictory.

        Args:
            uid: user id in mysql

        Returns:
            update_time: the message update time of a user. 
        """
        update_time = self.user_message.get_update_time_by_uid(uid)
        redis_dict.hset("user:"+str(uid),"update_time",update_time['update_time'])
        return update_time

    def init_message_to_all(self):
        """After server start, we should execuute this function to initial update time of every circles.

        Args:

        Returns:

        """
        result_list = self.circle_message.get_all_info()
        for value in result_list:
            ucid = value['cid']
            to_redis = value
            redis_dict.hmset("circle:"+ucid,to_redis)     

    def add_new_message_queue_to_all(self,cid):
        """After we create a new circle, we should initial its information to redis distory.

        Args:
            mc_id: message circle id. after ceate a new circle will get it.
        """
        entity = self.circle_message.get_info_by_cid(cid)
        redis_dict.hmset("circle:"+str(cid),entity)

    def deal_message_to_one(self,mid,uid):
        """ Deal a new message which is to a special user.
        We should save it in ac_message_table,ac_message_user_table
        then add this message to redis dictory of a special user..

        Args:
            mid: message id in ac_message_tabel
            uid: user id

        Returns:
            error or ok.[todo]
        """
        # in normal return 1.
        result = self.user_message.set_update_message_by_uid(uid,mid)
        if redis_dict.hexists("user:" + str(uid),"_xsrf"):
            # update user update_time.
            update_time = time.strftime(self.format_time,time.localtime())
            redis_dict.hset("user:"+str(uid),"update_time",update_time)

    def deal_message_to_many(self,mid,uid_list):
        """Deal a new message which is to a user list.
        We should save it in ac_message_table,ac_message_user_table
        then add this message to redis dictory to all of user referenced.

        Args:
            mid: message id in ac_message_tabel
            uid_list: all of user referenced.

        Returns:
            error or ok.[todo]       
        """
        uid_list = self.custom_list_to_list(uid_list)
        for value in uid_list:
            self.deal_message_to_one(mid,value)

    def deal_message_to_all(self,mid,cid):
        """Deal a new message which is to all of user belong to a circle.
        We should save it in ac_message_table,ac_circle_mesage_table.
        then add this message to redis dictory to all of circle referenced.
        Args:
            mid: message id in ac_message_tabel
            cid: circle_id in ac_circle_table

        Returns:
            error or ok.[todo]       
        """
        logging.info("deal message to all cid %s mid %s"%(cid,mid))
        result = self.circle_message.set_update_message_by_cid(cid,mid)
        message_update = redis_dict.hget("circle:"+str(cid),"message_queue")
        message_update = message_update+str(mid) + "_"
        redis_dict.hset("circle:"+str(cid),"message_queue",message_update)
        
    def custom_list_to_list(self,custom_list):
        """We define list as "_item_item_item", this function change it to python list.
        
        Args:
            custom_list: custom list we define.

        Returns
            message_list: python list.
        """
        custom_list = custom_list.split('_')
        message_list = ''
        print custom_list
        del custom_list[0]
        del custom_list[-1]
        if custom_list != '':
            message_list = [string.atoi(elem) for elem in custom_list]
        return message_list


    def __time_check_unit(self,last_update_time,update_time_now):
        """Campare last update time and update time now.

        Args:
            last_update_time:
            update_time_now:

        Returns:
            True: If update time now is later than last update time. return True
            False: else return false.
        """
        logging.info("update_time_now %s"%update_time_now)  
        strp_now = time.strptime(str(update_time_now),self.format_time)
        strp_last = time.strptime(last_update_time,self.format_time)
        result = time.mktime(strp_now) - time.mktime(strp_last)
        if result >= 0:            
            return True
        else:
            return False

    def check_and_get_message(self,uid,my_circle_list,last_update_time):
        """Find user's update message [include circle message and user message.]

        Args:
            uid: user id
            last_update_time: request from client, last time user send a message.
            my_circle_list:  request from client, the circle id user has join in.
        Returns:
            message_list 
        """
        update_time_now = redis_dict.hget("user:"+str(uid),"update_time")
        last_update_time = redis_dict.hget("user:"+str(uid),"last_update_time")
        if self.__time_check_unit(last_update_time,update_time_now) >= 0:
            # this update time is latter than last time, we should send message to client.
            message_list = {"user":[],"circle":[]}
            message_id_list = self.user_message.get_message_queue_by_uid(uid)['message_queue']
            #print "message _list is " + str(message_id_list)
            circle_list = self.custom_list_to_list(my_circle_list)
            #print "circle list [after change ]is %s"%circle_list
            circle_message_id_list = '_'
            for cid in circle_list:
                #print "uid :" + str(uid) + " cid " + str(cid) + " update time : "+ str(last_update_time)
                # the update time now of a sepcial circle.
                update_time_now = redis_dict.hget("circle:"+str(cid),"update_time")
                #print "update_time_now: "+ str(update_time_now)
                if self.__time_check_unit(last_update_time,update_time_now):
                    # this circle has been updated
                    result_str = self.circle_message.get_message_queue_by_cid(cid)['message_queue']
                    circle_message_id_list += result_str[1:]# delete the first char '_'
            if message_id_list != '_':
                # get user message content.
                message_id_list = self.custom_list_to_list(message_id_list)
                message_list['user'] = self._message.get_message_by_mid_list(message_id_list) 
                logging.info(" message list user : %s"%message_list['user'])   
            if circle_message_id_list != '_':
                # get ciecle message content.
                #print 'circle message id list is %s'%circle_message_id_list
                circle_message_id_list = self.custom_list_to_list(circle_message_id_list)
                # [todo]: if circle message can be repeated, use set to delete it.
                #print "circle list before: "+str(circle_message_id_list)
                #circle_message_id_list = list(set(circle_message_id_list))
                #print "circle list  after: "+str(circle_message_id_list)                
                message_list['circle'] = self._message.get_message_by_mid_list(circle_message_id_list,last_update_time) 
            result_message_list = []
            amount = 0
            tempcount = 0
            def __message_fileter(unit):
                if unit['type'] != 2:
                    return unit
                else:
                    if unit['message']['apply_uid'] != uid:
                        return unit

            for value in message_list['user']:
                # change time format
                # logging.info("value is : %s"%value)
                value['update_time'] = value['update_time'].strftime(self.format_time)
                # change dictory string to dictory object
                value['message'] = eval(value['message'])
                result_message_list.append(value)
            for value in message_list['circle']:
                # change time format
                # logging.info("value is : %s"%value)
                value['update_time'] = value['update_time'].strftime(self.format_time)
                # change dictory string to dictory object
                value['message'] = eval(value['message'])
                result_message_list.append(value)        
            result_message_list = filter(__message_fileter,result_message_list)    
            return result_message_list
        return []

    def return_message_check(self,uid):
        """Check the status. If client receive the message or not. if not, resend it.
        
        Args:
            code: 
                0 : receive failed. 1 receive success.
            uid: user id
            last_update_time: request from client, last time user send a message.
            my_circle_list:  request from client, the circle id user has join in.

        Returns:
        
        [version 2.0]
            just clear message queue of user. and update "last update time"
        """
        #if code ==0:
            # send message again.
        #    return self.update_check(uid,my_circle_list,last_update_time)
        #elif code == 1:
            # clear message queue.
        self.user_message.clear_message_queue(uid)
        last_update_time = time.strftime(self.format_time,time.localtime())
        redis_dict.hset("user:"+str(uid),"last_update_time",last_update_time)

    def find_user_message(self,uid):
        """Send all of message in message_queue to client.
        [deleted]: replaced by check_and_get_message
        Args:
            uid: user id.

        Returns:
            message_content_list:[json string]
                example:
                    [{'message': u'{test}', 'type': 1}, 
                    {'message': u'{test}', 'type': 1}, 
                    {'message': u'{test}', 'type': 1}]
        """
        message_list = self.user_message.get_message_queue_by_uid(uid)
        message_list = self.custom_list_to_list(message_list['message_queue'])
        print "send message before delete :%s"%message_list
        return self._message.get_message_by_mid_list(message_list)    

 
    def update_check_user(self,id_type,uid,id,last_update_time):
        """ check if update_time in server has been updated.
        Check the user in client's last update time, compare it to server.
        if last_update_time is early then update_time now. we should execute send_message
        [deleted]: replaced by check_and_get_message
        Args:
            uid: user id.
            last_update_time: client's last update time.
            id_type:string: "circle:" or "user:"

        Returns:
            True or false.
        """
        update_time_now = redis_dict.hget(id_type+str(uid),"update_time")
        print "update_time_now : %s"%update_time_now
   
        strp_now = time.strptime(update_time_now,self.format_time)
        strp_last = time.strptime(last_update_time,self.format_time)
        result = time.mktime(strp_now) - time.mktime(strp_last)
        if result >= 0:
            # this update time is latter than last time, we should send message to client.
            return True
        else:
            return False

    def send_message_to_all(self,uid,my_circle_list,last_update_time):
        """ Check user's circle has update or not.
        [deleted]: replaced by check_and_get_message
        Args:
            my_circle_list: user's circle list.

        Returns:
            result_message_dict: a list dictory,return all of circle's update informations
        """

        result_message_dict = {}
        print "in send message  to all"
        for cid in circle_list:
            print "uid :" + str(uid) + " cid " + str(cid) + " update time : "+ str(last_update_time)
            redis_dict.hget("circle:"+str(cid),"update_time")
            if self.update_check("circle:",uid,cid,last_update_time):
                self.send_message_to_all(cid,last_update_time)
                circle_message_list = self.circle_message.get_message_queue_by_cid(cid,last_update_time)
                result_message_dict[cid] = circle_message_list
        return result_message_dict

    def update_check_circle(self,cid,last_update_time):
        """
        [deleted]: replaced by check_and_get_message
        """
        update_time_now = redis_dict.hget("circle:"+cid,"update_time")
        print "update_time_now : %s"%update_time_now
   
        strp_now = time.strptime(update_time_now,self.format_time)
        strp_last = time.strptime(last_update_time,self.format_time)
        result = time.mktime(strp_now) - time.mktime(strp_last)
        if result >= 0:
            # this update time is latter than last time, we should send message to client.
            return True
        else:
            return False