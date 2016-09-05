#!usr/bin/env python
# -*- coding: utf-8 -*-  
# ec_user.py
from datetime import datetime
import time
import json
import string
from elasticsearch import Elasticsearch
class ElasticUserModule(object):
    def __init__(self,elasticsearch):
        self.ec = elasticsearch
        self._index = "alumnuscircle"
        self._type = "user"
    def createInfo(
        self,uid,faculty,major,name,country,state,city,admission_year,icon_url="default",job="student",
        company="the seu"):
        """
            "icon_url" : { "type" : "string", "index" : "not_analyzed" },
            "faculty": {"type" : "string","index": "not_analyzed"},
            "major": {"type":"string","index":"not_analyzed"},
            "name":{"type":"string","index":"not_analyzed"},
            "job":{"type":"string","analyzer":"ik_smart"},
            "country":{"type":"string","analyzer":"ik_smart"},
            "state":{"type":"string","analyzer":"ik_smart"},
            "city":{"type":"string","index":"not_analyzed"},
            "instroduction":{"type":"string","analyzer":"ik_smart"},
            "company":{"type":"string","analyzer":"ik_smart"},
            "job_list":{"type":"string","analyzer":"ik_smart"},
            "register_time":{"type":""}
        """
        format_time = "%Y-%m-%d %H:%M:%S"
        registertime = time.strftime(format_time,time.localtime())
        body= {
            "icon_url":icon_url,
            "faculty":faculty,
            "major":major,
            "name":name,
            "country":country,
            "state":state,
            "city":city,
            "job":job,
            "company":company,
            "register_time":registertime,
            "admission_year":admission_year
        }
        return self.ec.create(index=self._index,doc_type="user",id=uid,body=body)

    def updateinfo(self,body,uid):
        """Update user's information in elasticsearch

        all of parameter can not been error, if it not been updated. just post its original data.

        Args:
            uid:
            icon_url
            job
            instroduction
            company
            job_list
            tag

        Returns:

        """
        """
        body= {
            "icon_url":icon_url,
            "name":name,
            "country":country,
            "state":state,
            "city":city,
            "job":job,
            "company":company,
            "register_time":registertime,
            "job_list":job_list
        }
        """
        return self.ec.create(index=self._index,doc_type="user",id=uid,body=body)

    def get_all_user(self):
        body={
            "query":{"match_all":{}},
            "sort":{"register_time":{"order":"desc"}}
        }
        res = es.search(index=self._index,doc_type=self._type, body=body)
        return res

    def keyword_search(
        self,q,filter_admission_year_min=0,filter_admission_year_max=2009,
        filter_major_list=[u'_软件学院_软件工程_',u'_机械学院_机械工程_'],filter_city_list=[u'_中国_福建_漳州',u'_美国_']):
        #admission_year_query = self.set_admission_filter(filter_admission_year_min,filter_admission_year_max)
        body={
            "query":{
                    "filtered":{
                        "query":{
                            "multi_match": {
                                "query":q,
                                "fields":[ "faculty", "major","name","country","state","city","job","instroduction","company","job_list"],
                            }
                        },
                        "filter":{
                            "bool":{
                                "must": []
                            }
                        }

                }
            }
        }
        self.set_city_filter(body["query"]["filtered"]["filter"]["bool"]["must"],filter_city_list)
        self.set_major_filter(body["query"]["filtered"]["filter"]["bool"]["must"],filter_major_list)
        self.set_admission_filter(
            body["query"]["filtered"]["filter"]["bool"]["must"],
            filter_admission_year_min,filter_admission_year_max)
        res = es.search(index=self._index,doc_type=self._type, body=body)
        print json.dumps(body,)
        return res
    
    def set_admission_filter(self,body,filter_admission_year_min=0,filter_admission_year_max=9999):
        result={"range":{
                    "admission_year":{
                        "gte":filter_admission_year_min,
                        "lt":filter_admission_year_max
                    }
                }}
        body.append(result)
        return body
    def custom_list_to_list(self,custom_list):
        """We define list as "_item_item_item", this function change it to python list.
            [todo]:change this fucntion as a common function.
        Args:
            custom_list: custom list we define.

        Returns
            message_list: python list.
        """
        custom_list = custom_list.split('_')
        print custom_list
        del custom_list[0]
        del custom_list[-1]
        return custom_list

    def set_city_filter(self,body,filter_city_list):
        """
            body = body["query"]["filtered"]["filter"]["bool"]["must"]
        """
        result = {"bool":{"should":[]}}
        set_city_unit = [
            lambda x:{"term":{"country":x}},
            lambda x:{"term":{"state":x}},
            lambda x:{"term":{"city":x}}
        ]

        for city_string in filter_city_list:
            city_unit = self.custom_list_to_list(city_string)
            count = 0
            while count< len(city_unit):
                result['bool']['should'].append(set_city_unit[count](city_unit[count]))
                count+=1
        body.append(result)

    def set_major_filter(self,body,filter_major_list):
        result = {"bool":{"should":[]}}
        set_major_unit = [
            lambda x:{"term":{"faculty":x}},
            lambda x:{"term":{"major":x}}
        ]        
        for major_string in filter_major_list:
            major_unit = self.custom_list_to_list(major_string)
            count = 0
            while count< len(major_unit):
                result['bool']['should'].append(set_major_unit[count](major_unit[count]))
                count+=1
        body.append(result)

es = Elasticsearch()
model = ElasticUserModule(es)

"""
model.createInfo(uid=1,faculty=u"软件学院",major=u"软件工程",name=u"陈雄辉",country=u"美国",
    state=u"福建",city="漳州",admission_year=2010,icon_url="default",job=u"学生",instroduction="程勋,阿里的两份offer",
        company="东南大学",job_list="曾经去了google,腾讯")
model.createInfo(uid=1,faculty=u"软件学院",major="软件工程",name="陈雄晖",country="中国",
    state="福建",city="漳州",admission_year=2010,icon_url="default",job=u"学生",instroduction="程勋,阿里的两份offer",
        company="东南大学",job_list="曾经去了google,腾讯")

model.createInfo(uid=1,faculty=u"机械学院",major="机械工程",name="赵鹏青",country="中国",
    state="福建",city="漳州",admission_year=2011,icon_url="default",job="学生",instroduction="程勋,阿里的两份offer",
         company="东南大学",job_list="曾经去了google,腾讯")

model.createInfo(uid=1,faculty="软件学院",major="软件工程",name="陈雄辉",country="中国",
    state="福建",city="漳州",admission_year=2012,icon_url="default",job="学生",instroduction="程勋,阿里的两份offer",
        company="东南大学",job_list="曾经去了google,腾讯")
model.createInfo(uid=1,faculty="软件学院",major="软件工程",name="陈雄辉",country="china",
    state="福建",city="漳州",admission_year=2013,icon_url="default",job="学生",instroduction="程勋,阿里的两份offer",
        company="东南大学",job_list="曾经去了google,腾讯")
model.createInfo(uid=1,faculty="软件学院",major="软件工程",name="陈雄辉",country="china",
    state="福建",city="漳州",admission_year=2014,icon_url="default",job="学生",instroduction="程勋,阿里的两份offer",
        company="东南大学",job_list="曾经去了google,腾讯")
model.createInfo(uid=1,faculty="软件学院",major="软件工程",name="陈雄辉",country="china",
    state="福建",city="漳州",admission_year=2015,icon_url="default",job="学生",instroduction="offer",
        company="东南大学",job_list="曾经去了google,腾讯")
"""
#result = json.dumps(model.keyword_search("软件学院 陈雄辉",filter_admission_year_max=2019,ensure_ascii=False)
#print result 