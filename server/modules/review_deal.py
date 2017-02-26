#!usr/bin/env python
# coding=utf-8
# message_deal.py
import logging
import ConfigParser
from base import BaseModule
from common.variables import AP

class ReviewCircleModule(BaseModule):
    def __init__(self,db):
        BaseModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._manual_review_table =self.prefix+'manual_review_table'

        self._review_id = config.get(self._manual_review_table,"review_id")
        self._circle_name = config.get(self._manual_review_table,"circle_name")
        self._circle_icon_url = config.get(self._manual_review_table,"circle_icon_url")
        self._creator_uid = config.get(self._manual_review_table,"creator_uid")
        self._circle_type_id = config.get(self._manual_review_table,"circle_type_id")
        self._reason_message = config.get(self._manual_review_table,"reason_message")
        self._result = config.get(self._manual_review_table,"result")
        self._description = config.get(self._manual_review_table,"description")
        self._circle_type_name = config.get(self._manual_review_table,"circle_type_name")
        self._creator_name = config.get(self._manual_review_table,"creator_name")

    def set_new_review_message(self,circle_name,circle_icon_url,creator_uid,circle_type_name,reason_message,description,creator_name):
        """This method is to add new review circle message.
        client send parameters and it will store it to ac_manual_review_table.

        Args:
            circle_name
            circle_icon_url
            creator_uid
            circle_type_id
            reason_message
            [you can look for ac_manual_review_table to find the define all of those arguments.]
        Return:
            code[todo ]
            message
            
        """
        rm_id = self.db.insert("INSERT INTO " + self._manual_review_table + "( " + self._circle_name +" , "+
            self._circle_icon_url + " , " + self._creator_uid 
            + " , "+  self._circle_type_name + " , " + self._reason_message + 
            " , " + self._description + " , "+ self._creator_name+" ) " + "VALUES (%s,%s,%s,%s,%s,%s,%s)",
            circle_name,circle_icon_url,creator_uid,circle_type_name,reason_message,description,creator_name)
        return rm_id

    def update_review_result(self,result,review_id):
        result = self.db.update(
            "UPDATE " + self._manual_review_table + " SET " + self._result + " = %s " + " WHERE " + self._review_id + " = %s",int(result),int(review_id))
       #  logging.info("UPDATE " + self._manual_review_table + " SET " + self._result + " = " + result + "WHERE " + self._review_id + " = %s"%review_id)
        return result

    def get_review_list(self,result,max_id,limit_num):
        """get all information of manual review list.

        Args:
            result: 
                0 means return all of review list which still not solved.
                1 means return all of review list which has been solved,
            max_id:
                the review_id in the last entities.
            limit_num:
                the max number of return entities
        Returns:
            review list or []
        """
        if result == 0:
            symbol = '='
        else:
            symbol = '>'
        logging.info( "SELECT * FROM " + self._manual_review_table + " WHERE "+ self._review_id + 
            "< " + str(max_id) + " AND " + self._result + symbol+" 0   ORDER BY "+ self._manual_review_table + "."+self._review_id +" DESC LIMIT "+str(limit_num))
      
        result_list = self.db.query(
            "SELECT * FROM " + self._manual_review_table + " WHERE "+ self._review_id + 
            "< %s  AND " + self._result + symbol+" 0   ORDER BY "+ self._manual_review_table + "."+self._review_id +" DESC LIMIT %s",max_id,int(limit_num))
        return result_list

    def get_review_by_id(self,review_id):
        result = self.db.get(
            "SELECT *  FROM " + self._manual_review_table + " WHERE " + self._review_id + 
            " = %s LIMIT 1",review_id)
        return result