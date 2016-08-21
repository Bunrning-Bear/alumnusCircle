#!/usr/bin/env python
# coding=utf-8
# user_module.py
import ConfigParser
from common.variables import AP
import logging
from base import BaseModule
#[todo]:2016.8.21: all of global variables should be saved in variables.py not conf.ini
"""
    all of user module should inherit to this module.
    this module define some common data member
"""
class UserModule(BaseModule):
    def __init__(self,db):
        BaseModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._user_table = self.prefix+'user_common_info'
        self._uid = config.get(self._user_table,"uid")
        self._admission_year = config.get(self._user_table,"admission_year")
        self._faculty_id = config.get(self._user_table,"faculty_id")
        self._major_id = config.get(self._user_table,"major_id")
        self._name = config.get(self._user_table,"name")
        self._gender = config.get(self._user_table,"gender")
        self._job = config.get(self._user_table,"job")
        self._icon_url = config.get(self._user_table,"icon_url")
        self._city = config.get(self._user_table,"city")

"""
UserInfoModule is a Module operate to mysql table ac_user_base_info
"""
class UserInfoModule(UserModule):
    def __init__(self,db):
        UserModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._user_table = self.prefix+'user_base_info'
        self._user_access_token = config.get(self._user_table,"access_token")
        self._user_password = config.get(self._user_table,"password")
        self._user_phone = config.get(self._user_table,"phone")     
        self._user_stu_id = config.get(self._user_table,"stu_id")
        self._user_update_time = config.get(self._user_table,"update_time")
        
    def get_info_from_phone(self,phone):
        """Get all of user information from user_table.
        
        Args:
            phone: the phone user write.

        Returns:
            a dict mapping key to corresponding row data fetch.
            if there are not such user phone, return []
        """
        entity = self.db.query("SELECT * FROM " + self._user_table + " WHERE "+ self._user_phone +" = %s LIMIT 1",phone)
        return entity

    def find_user_phone(self,phone):
        """Get all of user

        """
        entity = self.db.query("SELECT * FROM " + self._user_table + " WHERE "+ self._user_phone +" = %s LIMIT 1",phone)
        hasRegister = True
        if entity == []:
            hasRegister = False
        return hasRegister

    def set_info_to_user(
        self,access_token,passwd,user_phone,stu_id):
        """Set user information into user table
        
        Args:
            access_token: the access_token get from Umeng.
            name: user name
            passwd: user' password 
            phone: user's phone number

        Returns:
            return user_id in user_base_info table of this user.
        """        
        author_id = self.db.execute(
            "INSERT INTO " + self._user_table + " ( " + self._user_access_token + " , "
            + self._user_password + " , " + self._user_phone+
            " , " + self._user_stu_id  + " )" +
            "VALUES (%s, %s, %s, %s )",access_token,  passwd, int(user_phone), str(stu_id))
        return author_id

    def update_time_from_user_id(self,uid,update_time):
        pass

"""
UserListModule is a module operate mysql table: ac_user_list_info
"""
class UserListModule(UserModule):
    def __init__(self,db):
        UserModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._user_table = self.prefix+'user_list_info'
        self._list_id = config.get(self._user_table,"list_id")
        self._publicity_level = config.get(self._user_table,"publicity_level")
       # self._my_circle_list = config.get(self._user_table,"my_circle_list")
       # self._job_list = config.get(self._user_table,"job_list")
       # self._contact_list = config.get(self._user_table,"contact_list")

    def set_info_to_user(self,uid,admission_year,faculty_id,major_id,name,gender,job,icon_url,city):
        """Insert new user to mysql, this function only use when register.
        
        Args:
            all of parameter name are the same to field in mysql table: ac_user_list_info. 
            please look for detail.

        Returns:
            return list_id in user_list_info table of this user.
        """
        author_id = self.db.execute(
            "INSERT INTO " + self._user_table + " ( " + self._uid + " , "
            + self._admission_year + " , " + self._faculty_id+
            " , " + self._major_id  + " , " + self._name+
            " , " + self._gender+ " , " + self._job+
            " , " + self._icon_url+ " , " +self._city+
            " )" +
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )",
            uid,admission_year,faculty_id,major_id,name,gender,job,icon_url,city)
        return author_id


"""
UserListModule is a module operate mysql table: ac_user_detail_info
"""
class UserDetailModule(UserModule):
    def __init__(self,db):
        UserModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._user_table = self.prefix+'user_detail_info'
        self._detail_id = config.get(self._user_table,"detail_id")
        self._company = config.get(self._user_table,"company")
        self._my_circle_list = config.get(self._user_table,"my_circle_list")
        self._job_list = config.get(self._user_table,"job_list")
        self._contact_list = config.get(self._user_table,"public_contact_list")
        self._contact_list = config.get(self._user_table,"protect_contact_list")

    def set_info_to_user(
        self,uid,admission_year,faculty_id,major_id,name,gender,job,icon_url,city,company):
        """Insert new user to mysql, this function only use when register.
        
        Args:
            all of parameter name are the same to field in mysql table: ac_user_detail_info. 
            please look for detail.

        Returns:
            return detail_id in user_detail_info table of this user.
        """
        author_id = self.db.execute(
            "INSERT INTO " + self._user_table + " ( " + self._uid + " , "
            + self._admission_year + " , " + self._faculty_id+
            " , " + self._major_id  + " , " + self._name+
            " , " + self._gender + " , "  + self._job+
            " , " + self._icon_url + " , " + self._city+
            " , " + self._company + 
            " )" +
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            uid,admission_year,faculty_id,major_id,name,gender,job,icon_url,city,company)
        return author_id

    def get_info_from_uid(self,uid):
        """Get all of information in user_detail_info table.
        Args:
            uid[int]: user id in user_base_info

        Returns:
            a dictory store all of information in mysql, if not find in mysql, will return []
        """
        entity = self.db.query("SELECT * FROM " + self._user_table + " WHERE "+ self._uid +" = %s LIMIT 1",uid)
        return entity