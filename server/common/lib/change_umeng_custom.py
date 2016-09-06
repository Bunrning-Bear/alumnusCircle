# change_umeng_custom.py
import json

def change_custom_string_to_json(self,dic):
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


dic = {"message": "get umeng api successfully", "code": 0, "Data":{"update": {}, "response": {"count": 10, "total": 8, "page": 1, "results": [{"liked": False, "seq": 3583942, "creator": {"icon_url": {}, "medal_ids": [], "id": "57cd37cfb9a9967eb0367d76", "source_uid": "15996198251", "name": "15996198251"}, "topics": [{"stats": "empty", "description": "the circle will be beautiful!", "icon_url": {"origin": "empty", "80": "empty", "160": "empty"}, "image_urls": [], "custom": "{\"virtual_cid\": \"57c69d67d36ef3151eb80ba9\", \"creator_uid\": \"123\"}", "id": "57c69d68d36ef3151eb80bac", "name": "new circle 983"}], "tag": 0, "readable_create_time": "13:56", "id": "57ce5a7ad36ef3c9e5153d70", "stats": {"liked": 0, "forwards": 0, "comments": 0}, "title": "circle feed list !", "origin_feed": "empty", "custom": "", "content": "this is a feed !yeah~~ 38516", "source": "\u793e\u533a", "location": {}, "media_type": 0, "type": 0, "status": 0, "is_topic_top": "empty", "image_urls": [{"origin": "http://test.jpg", "phone": "http://test.jpg", "750": "http://test.jpg", "360": "http://test.jpg"}], "is_top": 0, "topic_tag": "", "related_users": "empty", "has_collected": False, "create_time": "2016-09-06 13:56:10", "parent_feed_id": "", "is_recommended": False, "share_link": "http://wsq.umeng.com/feeds/57ce5a7ad36ef3c9e5153d70/"}, {"liked": False, "seq": 3583940, "creator": {"icon_url": {}, "medal_ids": [], "id": "57cd37cfb9a9967eb0367d76", "source_uid": "15996198251", "name": "15996198251"}, "topics": [{"stats": "empty", "description": "the circle will be beautiful!", "icon_url": {"origin": "empty", "80": "empty", "160": "empty"}, "image_urls": [], "custom": "{\"virtual_cid\": \"57c69d67d36ef3151eb80ba9\", \"creator_uid\": \"123\"}", "id": "57c69d68d36ef3151eb80bac", "name": "new circle 983"}], "tag": 0, "readable_create_time": "13:55", "id": "57ce5a64b9a9965c03f6b679", "stats": {"liked": 0, "forwards": 0, "comments": 0}, "title": "circle feed list !", "origin_feed": "empty", "custom": "", "content": "this is a feed !yeah~~ 79037", "source": "\u793e\u533a", "location": {}, "media_type": 0, "type": 0, "status": 0, "is_topic_top": "empty", "image_urls": [{"origin": "http://test.jpg", "phone": "http://test.jpg", "750": "http://test.jpg", "360": "http://test.jpg"}], "is_top": 0, "topic_tag": "", "related_users": "empty", "has_collected": False, "create_time": "2016-09-06 13:55:48", "parent_feed_id": "", "is_recommended": False, "share_link": "http://wsq.umeng.com/feeds/57ce5a64b9a9965c03f6b679/"}]}}}
dict2 = "{\"virtual_cid\": \"57c69d67d36ef3151eb80ba9\", \"creator_uid\": \"123\"}"
change_custom_string_to_json(dic)

print json.dumps(dic)
