#!/usr/bin/env python
# coding=utf-8
# user_module.py
import ConfigParser
from common.variables import AP
import logging
from base import BaseModule
#[todo]:2016.8.21: all of global variables should be saved in variables.py not conf.ini
#[todo]:2016.8.21:all of three class should add to userModule.
"""
    all of user module should inherit to this module.
    this module define some common data member
"""
class UserModule(BaseModule):
    def __init__(self,db):
        BaseModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._user_common_table = self.prefix+'user_common_info'
        self._uid = config.get(self._user_common_table,"uid")
        self._admission_year = config.get(self._user_common_table,"admission_year")
        self._faculty = config.get(self._user_common_table,"faculty")
        self._major = config.get(self._user_common_table,"major")
        self._name = config.get(self._user_common_table,"name")
        self._gender = config.get(self._user_common_table,"gender")
        self._job = config.get(self._user_common_table,"job")
        self._icon_url = config.get(self._user_common_table,"icon_url")
        self._city = config.get(self._user_common_table,"city")
        self._state = config.get(self._user_common_table,"state")
        self._country =config.get(self._user_common_table,"country")


    def update_optional_argu_unit(self,argu):
        return argu + "= %s"

    def update_optional_argu(self,table,dic_argu):
        update = "UPDATE " + table + " SET "
        assignment = ''
        for key,value in dic_argu.items():
            assignment = assignment + self.update_optional_argu_unit(key) + " , "
        return update + assignment[:-2]

    def update_filter(self,dic):
        """filter useless dic key of request, just hold those useful which define by __changed_allowed list

        """
        dic_return = {}
        for value in self._change_allowed:
           if  dic.has_key(value):
                dic_return[value] = dic[value]
        return dic_return

    def update_info_to_user(self,dic,uid):
        """
        """
        dic = self.update_filter(dic)
        sql = self.update_optional_argu(self._user_table, dic)
        temp_list = []
        for key,value in dic.items():
            temp_list.append(str(value))
        temp_list.append(str(uid))
        para = tuple(temp_list)

        sql =sql + "WHERE "+ self._uid + " = %s"
        logging.info("sql is : %s  %s"%(sql,para))
        return self.db.updatemany(sql,[para])


"""
UserInfoModule is a Module operate to mysql table ac_user_base_info
"""
class UserInfoModule(UserModule):
    def __init__(self,db):
        UserModule.__init__(self,db)
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP+'common/conf.ini'))
        self._user_base_table = self.prefix+'user_base_info'
        self._user_access_token = config.get(self._user_base_table,"access_token")
        self._user_password = config.get(self._user_base_table,"password")
        self._user_phone = config.get(self._user_base_table,"phone")     
        self._user_stu_id = config.get(self._user_base_table,"stu_id")
        self._user_update_time = config.get(self._user_base_table,"update_time")
        self._user_adlevel = config.get(self._user_base_table,"adlevel")
        self._umeng_id = config.get(self._user_base_table,"umeng_id")
        
    def get_info_from_phone(self,phone):
        """Get all of user information from user_table.
        
        Args:
            phone: the phone user write.

        Returns:
            a dict mapping key to corresponding row data fetch.
            if there are not such user phone, return []
        """
        entity = self.db.query("SELECT * FROM " + self._user_base_table + " WHERE "+ self._user_phone +" = %s LIMIT 1",phone)
        return entity

    def find_user_phone(self,phone):
        """Get all of user

        """
        entity = self.db.query("SELECT * FROM " + self._user_base_table + " WHERE "+ self._user_phone +" = %s LIMIT 1",phone)
        hasRegister = True
        if entity == []:
            hasRegister = False
        return hasRegister

    def get_umeng_id_from_uid(self,uid):
        """Get user's umeng id from mysql.
        to execute some ooperate which need umeng id in umeng api

        Args:
            uid

        Returns:

        """
        entity = self.db.get(
            "SELECT "+ self._umeng_id +
            " FROM " + self._user_base_table + 
            " WHERE "+ self._uid  +" = %s LIMIT 1",
            uid)
        return entity['umeng_id']

    def get_access_token_from_uid(self,uid):
        """Get user's access_token from mysql.
        to execute some operate in umeng.

        Args:
            uid:

        Returns:
            access_token
        """
        entity = self.db.get(
            "SELECT "+ self._user_access_token +
            " FROM " + self._user_base_table + 
            " WHERE "+ self._uid  +" = %s LIMIT 1",
            uid)
        logging.info("entity of access_token is %s"%entity)
        return entity

    def set_info_to_user(
        self,access_token,passwd,user_phone,stu_id,adlevel=0):
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
            "INSERT INTO " + self._user_base_table + " ( " + self._user_access_token + " , "
            + self._user_password + " , " + self._user_phone+
            " , " + self._user_stu_id  + " , "+ self._user_adlevel + " )" +
            "VALUES (%s, %s, %s, %s,%s )",access_token,  passwd, int(user_phone), str(stu_id),adlevel)
        return author_id

    def update_umeng_id(self,umeng_id,uid):
        logging.info
        logging.info("update umeng id is :" +" UPDATE " + self._user_base_table + 
    " SET " + self._umeng_id + " = "+ str(umeng_id) +"WHERE " + self._uid + " = " + str(uid))
        entity = self.db.update(
            "UPDATE " + self._user_base_table + 
            " SET " + self._umeng_id + " = %s WHERE " + self._uid + " = %s",
            str(umeng_id),uid)

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
        self._change_allowed = (self._job, self._icon_url,self._city,self._publicity_level)


    def set_info_to_user(self,uid,admission_year,faculty_id,major_id,name,gender,job,icon_url,city,state,country):
        """Insert new user to mysql, this function only use when register.
        
        Args:
            all of parameter name are the same to field in mysql table: ac_user_list_info. 
            please look for detail.

        Returns:
            return list_id in user_list_info table of this user.
        """
        logging.info("icon_url %s"%icon_url)
        author_id = self.db.execute(
            "INSERT INTO " + self._user_table + " ( " + self._uid + " , "
            + self._admission_year + " , " + self._faculty+
            " , " + self._major  + " , " + self._name+
            " , " + self._gender+ " , " + self._job+
            " , " + self._icon_url+ " , " +self._city+ " , " +self._state+ " , " +self._country +
            " )" +
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s , %s , %s )",
            uid,admission_year,faculty_id,major_id,name,gender,job,icon_url,city,state,country)

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
        self._company_publicity_level = config.get(self._user_table,"company_publicity_level")
        self._my_circle_list = config.get(self._user_table,"my_circle_list")
        self._job_list = config.get(self._user_table,"job_list")
        self._job_list_level = config.get(self._user_table,"job_list_level")
        self._public_contact_list = config.get(self._user_table,"public_contact_list")
        self._protect_contact_list = config.get(self._user_table,"protect_contact_list")
        self._instroduction = config.get(self._user_table,"instroduction")
        self._user_last_update_time = config.get(self._user_table,"last_update_time")
        self._create_circle_list = config.get(self._user_table,"create_circle_list")
        self._change_allowed = (
            self._job, self._icon_url,self._city,self._company,self._instroduction,
            self._job_list,self._public_contact_list,self._protect_contact_list,
            self._company_publicity_level,self._job_list_level)

    def set_info_to_user(
        self,uid,admission_year,faculty_id,major_id,name,gender,job,icon_url,city,state,country,company):
        """Insert new user to mysql, this function only use when register.
        
        Args:
            all of parameter name are the same to field in mysql table: ac_user_detail_info. 
            please look for detail.

        Returns:
            return detail_id in user_detail_info table of this user.
        """
        author_id = self.db.execute(
            "INSERT INTO " + self._user_table + " ( " + self._uid + " , "
            + self._admission_year + " , " + self._faculty+
            " , " + self._major  + " , " + self._name+
            " , " + self._gender + " , "  + self._job+
            " , " + self._icon_url + " , " + self._city+ " , " +self._state+ " , " +self._country + 
            " , " + self._company + 
            " )" +
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            uid,admission_year,faculty_id,major_id,name,gender,job,icon_url,city,state,country,company)
        return author_id

    def get_name_from_uid(self,uid):

        entity = self.db.query(
            "SELECT "+ self._name +" FROM " + self._user_table + " WHERE "+ self._uid +" = %s LIMIT 1",uid)
        return entity[0][self._name]

    def get_info_from_uid(self,uid):
        """Get all of information in user_detail_info table.
        Args:
            uid[int]: user id in user_base_info

        Returns: 
            a dictory store all of information in mysql, if not find in mysql, will return []
        """
        entity = self.db.query("SELECT * FROM " + self._user_table + " WHERE "+ self._uid +" = %s LIMIT 1",uid)
        entity = entity[0]
        entity['last_update_time'] = str(entity['last_update_time'])
        return entity

    def update_last_update_time_by_uid(self,uid,last_update_time):
        entity = self.db.update(
            "UPDATE " + self._user_table + 
            " SET " + self._user_last_update_time + " = %s WHERE " + self._uid + " = %s",
            last_update_time,uid)

    def add_create_circle_list(self,circle_id,uid):
        entity = self.db.update(
            "UPDATE "+ self._user_table + 
            " SET " + self._my_circle_list + " = CONCAT("+ self._create_circle_list  + ", %s ) "+ 
            "WHERE "+self._uid + "= %s",str(circle_id)+"_",uid)

        entity = self.db.update(
            "UPDATE "+ self._user_table + 
            " SET " + self._create_circle_list  + " = CONCAT("+ self._create_circle_list  + ", %s ) "+ 
            "WHERE "+self._uid + "= %s",str(circle_id)+"_",uid)

    def update_my_circle_list(self,circle_id,uid):
        entity = self.db.update(
            "UPDATE "+ self._user_table + 
            " SET " + self._my_circle_list + " = CONCAT("+ self._my_circle_list  + ", %s ) "+ 
            "WHERE "+self._uid + "= %s",str(circle_id)+"_",uid)

    def get_create_circle_list(self,uid):
        entity = self.db.query(
            "SELECT "+ self._create_circle_list +
            " FROM " + self._user_table + 
            " WHERE "+ self._uid +" = %s LIMIT 1",uid)
        return entity[0][self._create_circle_list]      

    def get_my_circle_list(self,uid):
        entity = self.db.query(
            "SELECT "+ self._my_circle_list +
            " FROM " + self._user_table + 
            " WHERE "+ self._uid +" = %s LIMIT 1",uid)
        return entity[0][self._my_circle_list]      

    def leave_circle(self,string_my_circle_list,string_create_circle_list,uid):
        entity = self.db.update(
            "UPDATE "+ self._user_table + 
            " SET " + self._my_circle_list + " = %s , "+ self._create_circle_list  + " = %s  "+ 
            "WHERE "+self._uid + "= %s",str(circle_id)+"_",uid)