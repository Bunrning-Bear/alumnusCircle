# user_module.py
#Author ChenXionghui
import ConfigParser
from common.variables import AP

class BaseModule(object):
    def __init__(self,db):
        self.__db = db
        self.prefix = "ac_"
    @property
    def db(self):
        return self.__db
