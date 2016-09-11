 #!/usr/bin/env python
 # coding=utf-8
 # message.py
import logging
import ConfigParser
import pdb

from base import BaseModule
from common.variables import AP
from base import BaseModule

class MessageModule(BaseModule):
    def __init__(self,db):
        BaseModule.__init__(self,db)
        self.prefix = self.prefix + 'message_'
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))


class MessageCircleModule(MessageModule):
    def __init__(self,db):
        MessageModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._circle_table =self.prefix+'circle_table'
        self._mc_id = config.get(self._circle_table,"mc_id")
        self._umeng_circle_id = config.get(self._circle_table,"umeng_circle_id")
        self._cid = config.get(self._circle_table,"cid")
        self._message_queue = config.get(self._circle_table,"message_queue")
        self._update_time = config.get(self._circle_table,"update_time")

    def set_circle_info(self,cid,umeng_circle_id):
        """Set circle info into message_circle_table.
        
        Args:
            cid:
            umeng_circle_id

        Returns:
            mc_id: message_circle_table_id
        """
        mc_id = self.db.execute(
            "INSERT INTO " + self._circle_table + " ( " + self._cid +" , " + self._umeng_circle_id + " ) "
             + " VALUES ( %s, %s)",
            cid,umeng_circle_id)
        return mc_id

    def get_all_info(self):
        """get all circle message information

        Args:
            none

        Returns:
            return all of circle table information
        """
        entities = self.db.query("SELECT * FROM "+self._circle_table)
        return entities

    def get_info_by_cid(self,cid):
        """get a special message circle table message by cid.

        Args:
            cid.

        Returns:
            the circle's message.
        """
        entities = self.db.get(
            "SELECT * FROM " + self._circle_table + 
            " WHERE "+ self._cid + " = %s",cid)
        return entities

    def set_update_message_by_cid(self,cid,message_id):
        entity = self.db.update(
            "UPDATE "+self._circle_table + 
            " SET " + self._message_queue + " = CONCAT("+self._message_queue + ", %s ) "+ 
            "WHERE "+self._cid + "= %s",str(message_id)+"_",cid) 
        return entity

    def get_message_queue_by_cid(self,cid):
        entity = self.db.get(
            "SELECT " + self._message_queue + 
            " FROM " +  self._circle_table + 
            " WHERE " + self._cid  + " = %s LIMIT 1",cid)
        return entity


"""
module of ac_user_message_table.
store entites the queue_list of a special user.
"""
class UserMessageModule(MessageModule):
    def __init__(self,db):
        MessageModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._user_message_table = self.prefix+'user_table'
        self._uid = config.get(self._user_message_table,"uid")
        self._um_id = config.get(self._user_message_table,"mu_id")
        self._message_queue = config.get(self._user_message_table,"message_queue")
        self._update_time = config.get(self._user_message_table,"update_time")

    def set_user_to_message(self,uid):
        """Set user's uid to ac_user_message_table. this function will be call only when user register.
        
        Args:
            uid: user id.

        Returns:
           um_id: the id [primary key] of ac_user_message_table    
        """
        um_id = self.db.execute(
            "INSERT INTO " + self._user_message_table + "( " + self._uid + " ) " + 
            "VALUES ( %s )",uid)
        return um_id
    def get_update_time_by_uid(self,uid):
        """get user's message update time. if message time has been updated. send message queue to client.
        this function will been call when user login.

        Args:
            uid: user id.

        Returns:
            update_time.
        """
        update_time = self.db.get(
            "SELECT update_time FROM " + self._user_message_table + 
            " WHERE " + self._uid + "= %s", uid)
        
        return update_time

    def set_update_message_by_uid(self,uid,message_id):
        """
        """
        entity = self.db.update(
            "UPDATE "+self._user_message_table + 
            " SET " + self._message_queue + " = CONCAT("+self._message_queue + ", %s ) "+ 
            "WHERE "+self._uid + "= %s",str(message_id)+"_",uid)
        return entity

    def get_message_queue_by_uid(self,uid):
        entity = self.db.get(
            "SELECT " + self._message_queue + 
            " FROM " + self._user_message_table + 
            " WHERE " +self._uid + " = %s LIMIT 1",uid)
        return entity

    def clear_message_queue(self,uid):
        entity = self.db.update(
            "UPDATE "+self._user_message_table + 
            " SET " + self._message_queue + " = '_' " + 
            "WHERE "+self._uid + "= %s",uid) 
        return entity


"""
module of ac_message_table.store all of messages.
"""
class MessagesListModule(MessageModule):
    def __init__(self,db):
        MessageModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._message_table = self.prefix+'table'
        self._mid =  config.get(self._message_table,"mid")
        self._type = config.get(self._message_table,"type")
        self._message = config.get(self._message_table,"message")
        self._update_time = config.get(self._message_table,"update_time")

    def set_message(self,message_type,message):
        """Set message to mysql. every time we create a message, we should store it in mysql.

        Args:
            type: message type. look databases.md for detail.
            message: the content of a special message.

        Returns:
            mid: the id [primary key] of ac_message_table    
        """
        # message = json.dumps(message)
        mid = self.db.execute(
            "INSERT INTO " + self._message_table + " ( "+ self._type + " , " + self._message + ")" + 
            " VALUES ( %s, %s ) ",message_type, str(message))
        return mid

    def get_message_by_mid_list(self,mid_list,update_time = 0):
        """Get all of message information of a mid_list.
        
        Args:
            mid_list: message id list .

        Returns: 
            message list.
        """
        count = 0
        where_str = ''
        logging.info("get meesage_by_mid_list %s "%mid_list)
        logging.info("get message by mid list , update time %s "%update_time)
        while count < len(mid_list):
            where_str = where_str + self._mid + "= %s OR "
            count +=1
        if update_time == 0:
            result = self.db.query(
                "SELECT "+ self._message + " , "+ self._type + " , " +  self._update_time + 
                " FROM " + self._message_table + 
                " WHERE " + where_str[:-3],*mid_list)
        else:
            mid_list.append(update_time)
            result = self.db.query(
                "SELECT "+ self._message + " , " + self._type + " , "+ self._update_time + 
                " FROM " + self._message_table + 
                " WHERE " + where_str[:-3] +  
                " AND UNIX_TIMESTAMP( " + self._update_time +" ) >= " + "UNIX_TIMESTAMP( %s )",*mid_list)
        return result