# change_umeng_custom.py
#Author ChenXionghui
import json

def change_custom_string_to_json(dic):
    for key,value in dic.items():
        print "in dictory : ",key,value
        if key == 'custom' and value !='':
            dic[key] = json.loads(value)
        if isinstance(value,dict):
            change_custom_string_to_json(value)
        elif isinstance(value,list):
            print " out of list ", value
            for list_value in value:
                print "in list : "+str(list_value)
                change_custom_string_to_json(list_value)

# https://rest.wsq.umeng.com/0/user?ak=57b18b2ee0f55ac368001dc8&uid=57cd37cfb9a9967eb0367d76
dic = {"id": "57cd37cfb9a9967eb0367d76", "source_uid": "15996198251", "source": "self_account", "name": "15996198251", "age": 1, "gender": 0, "atype": 0, "status": 0, "icon_url": {}, "level": 0, "level_title": "", "score": 0, "custom": "{\"city\": \"\\u6f33\\u5dde\", \"major\": \"\\u7ecf\\u6d4e\\u7ba1\\u7406\", \"state\": \"\\u798f\\u5efa\", \"uid\": 85, \"faculty\": \"\\u91d1\\u878d\", \"country\": \"\\u4e2d\\u56fd\", \"admission_year\": 2014, \"job\": \"student\", \"real_name\": \"\\u9648\\u96c4\\u8f89\", \"publicity_level\": 0}", "is_recommended": True, "has_followed": False, "stats": {"followings": 5, "feeds": 17, "fans": 0}, "medal_ids": []}
change_custom_string_to_json(dic)

print json.dumps(dic)
