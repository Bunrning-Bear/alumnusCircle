#!usr/bin/env python
# -*- coding: utf-8 -*-
# ex_test1.py
#urllibtest.py
# coding=utf-8
#Author ChenXionghui
from elasticsearch import Elasticsearch
import elasticsearch
es = Elasticsearch([{'host':'localhost','port':9200}])
body1={
    "mappings":{
        "user":{
            "properties":{
                "icon_url" : { "type" : "string", "index" : "not_analyzed" },
                "faculty": {"type" : "string","index" : "not_analyzed"},
                "major": {"type":"string","index" : "not_analyzed"},
                "name":{"type":"string","analyzer":"ik_smart"},
                "job":{"type":"string","analyzer":"ik_max_word"},
                "country":{"type":"string","index" : "not_analyzed"},
                "state":{"type":"string","index" : "not_analyzed"},
                "city":{"type":"string","index" : "not_analyzed"},
                "instroduction":{"type":"string","analyzer":"ik_max_word"},
                "company":{"type":"string","analyzer":"ik_max_word"},
                "job_list":{"type":"string","analyzer":"ik_max_word"},
                "register_time":{"type":"date","format":"yyyy-MM-dd HH:mm:ss"},
                "gender":{"type":"boolean"}
            }   
        }
    }
}
body2={
    "icon_url":1,
    "faculty":"soft",
    "major":"ware",
    "name":"chenxionghui",
    "job":"student",
    "city":"nanjing",
    "instroduction":"my instroduction",
    "company":"google",
    "job_list":"job1_job2",
    "gender":"12",
    "auth":"12323"
}
#res = es.create(index='alumnuscircle',doc_type="user",body=body1)

res = es.indices.create(index='alumnuscircle', body=body1)
print res
#res=client.create(index="alumnuscircle",body=body1)
# print res
#res = es.get_mapping(index='alumnuscircle')
#print help(es.get_mapping)

