#urllibtest.py
# coding=utf-8
import urllib2
import urllib
import cookielib
import json
import random
import hashlib
# prefix = "http://139.196.207.155:8000"
prefix = "http://127.0.0.1:8000 "
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
# get _xsrff
resp = urllib2.urlopen(prefix+'/')
the_page = resp.read()
print the_page

_xsrf = json.loads(the_page)['Data']['_xsrf']

def set_resquest(api,data,method):
    # data is dictory.
    # method can be get put delete post ?
    # get _xsrff
    for item in cj:
        if item.name == '_xsrf':
            _xsrf = item.value
    if method != 'GET':
        data['_xsrf'] = _xsrf
    data = urllib.urlencode(data)
    url = prefix + api
    if method == 'GET':
        url = url + "?"+ data
    request = urllib2.Request(url,data)
    request.get_method = lambda: method # or 'DELETE' 
    return request

def setMessage(message,num,content):
   message[num] = "No.%s "%num + content + "\r\n"

def set_info_json(dic):
    info_json = json.dumps

def do_request(api,dic,message,method,otherPara):
    count = 0
    while count < len(dic):
        info_json = json.dumps(dic[count])
        para = otherPara[count]
        para['info_json'] = info_json
        # print "do request :" + str(para) + str(ot)
        req = set_resquest(api,para,method)
        response = urllib2.urlopen(req)
        the_page = response.read()
        print message[count] + the_page
        count = count + 1   

def getcommentlist():
    api = '/get_my_comment'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
    }
    info_json[num] = {
        "count":30,
        "type":'received', # set 'received' as default. we can also set 'sent' to get all of comments I have sent.
        "page":1
    }
    message[num] = "my comment list : \n"    
    do_request(api,info_json,message,"POST",otherPara) 


def getmessage():
    api = '/getmessage'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
        'my_circle_list':'_14_'# POST or DELETE stand for like and cancel like
    }
    info_json[num] = {
    }
    message[num] = "my_circle_list: \n"    
    do_request(api,info_json,message,"POST",otherPara) 


def like():
    api='/like'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        'method':'POST'# POST or DELETE stand for like and cancel like
    }
    info_json[num] = {
        "feed_id":"57ce5a64b9a9965c03f6b679",
    }
    message[num] = "like \n"    
    num +=1
    otherPara[num] = {
        'method':'DELETE'# POST or DELETE stand for like and cancel like
    }
    info_json[num] = {
        "feed_id":"57ce5a64b9a9965c03f6b679",
    }    
    message[num] = "cancel like \n"    
    do_request(api,info_json,message,"POST",otherPara) 


def pub_comment():
    api='/pubcomment'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {

    }
    info_json[num] = {
        "feed_id":"57ce5a64b9a9965c03f6b679",
        "content":"this is a comment"+str(random.randint(1,1000))
    }
    message[num] = "pub comment  \n"    
    do_request(api,info_json,message,"POST",otherPara)     

def commit_list():
    api='/commentlist'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "feed_id":"57ce5a64b9a9965c03f6b679",
        "page":1,
        "count":30
    }
    info_json[num] = {
    }
    message[num] = "comment list \n"    
    do_request(api,info_json,message,"POST",otherPara)  


def feed_detail():
    api = '/feed_detail'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "feed_id":"57ce5a64b9a9965c03f6b679"
    }
    info_json[num] = {
    }
    message[num] = "feed deatail\n"    
    do_request(api,info_json,message,"POST",otherPara)  

def user_detail():
    api = '/user_detail'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "uid":97
    }
    info_json[num] = {
    }
    message[num] = "user deatail\n"    
    do_request(api,info_json,message,"POST",otherPara)     


def search():
    api='/search_user'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "filter_admission_year_min":2000,# 0 for not filter
        "filter_admission_year_max":2016,# 9999 for not filter
        "filter_major_list":json.dumps([]),#([u'_金融_',u'_软件学院_']), # [] for not filter
        "filter_city_list": json.dumps([]), # ([u'_中国_福建_漳州_']), # [] for not filter 
        "all_match":0,# 0 for not query search. 1 for query search 
        "query":""
    }
    info_json[num] = {
    }
    message[num] = "search,\n"    
    do_request(api,info_json,message,"POST",otherPara)     

def circle_member_list():
    api = '/circle_member_list'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
    }
    info_json[num] = {
        "count":1000,
        "topic_id":"57c69d68d36ef3151eb80bac",# this is the only circle can be use when test.
        "page":1
    }
    message[num] = "circle member list .\n"    
    do_request(api,info_json,message,"POST",otherPara) 


def circle_feed_list():
    api = '/circle_feed'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
    }
    info_json[num] = {
        "count":10,
        "topic_id":"57c69d68d36ef3151eb80bac",# this is the only circle can be use when test.
        "page":1,
        "order":0
    }
    message[num] = "feed of a special circle.\n"    
    do_request(api,info_json,message,"POST",otherPara) 

def update_feed():
    api ='/myfeed/update'
    info_json = {}
    message = {}
    otherPara = {}
    num = 0
    otherPara[num] = {
    }
    info_json[num] = {
            "content":"this is a feed !yeah~~ "+ str(random.randint(1,100000)),
            "topic_ids":"57c69d68d36ef3151eb80bac",
            "title":" circle feed list !",
            # "image_urls":[{'origin':'http://test1.jpg', '360':'http://test2.jpg', '750':'http://test3.jpg'}],
            "img_str":"http://test2.jpg;http://test3.jpg"
    }
    message[num] = "update a feed."    
    do_request(api,info_json,message,"POST",otherPara) 


def get_follow_list():
    api= '/followslist'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
    }
    info_json[num] = {
        "count":30,
        "page":1,
        "uid":85
    }
    message[num] = "get my circle list."    
    do_request(api,info_json,message,"POST",otherPara) 

def follow_test():
    api = '/follow'
    num = 0
    info_json = {}
    message = {}
    otherPara = {}
    otherPara[num] = {
        "target":"follow",
    }
    info_json[num] = {
        "target_uid":"57ce32e2d36ef3d9adcfce6f"
    }
    message[num] = "follow."
    num +=1
    otherPara[num] = {
        "target":"follow",
    }
    info_json[num] = {
        "target_uid":"57ce3064b9a996566bef6681"
    }
    message[num] = "follow."
    num +=1
    do_request(api,info_json,message,"POST",otherPara)    

def get_all_circle_test():
    api = '/get_my_circle'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    otherPara[num] = {}
    dic[num] = {
    }
    message[num] = "get my circle list."
    do_request(api,dic,message,"POST",otherPara)    

def get_my_filter_circle_test():
    api = '/get_my_filter_circle'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    otherPara[num] = {"my_filter_circle":"_14_"}
    dic[num] = {

    }
    message[num] = "get my admin circle list."
    do_request(api,dic,message,"POST",otherPara)   

def circle_apply_test(): 
    api ='/circle_apply_result'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    otherPara[num] = {"result":1,"apply_user":85,"circle_id":14}
    dic[num] = {
    }
    message[num] = "agree the user apply to the circle."
    do_request(api,dic,message,"POST",otherPara)
    """
    follow success:
    {
        "update": {
            
        },
        "response": {
            "stats": {
                "fans": 0,
                "feeds": 0
            },
            "description": "the circle will be beautiful!",
            "tags": [
                
            ],
            "icon_url": {
                "origin": null,
                "80": null,
                "160": null
            },
            "image_urls": [
                
            ],
            "custom": "{\"virtual_cid\": \"57c69d67d36ef3151eb80ba9\", \"creator_uid\": \"123\"}",
            "secret": false,
            "create_time": "2016-08-31 17:03:36",
            "has_followed": True,
            "id": "57c69d68d36ef3151eb80bac",
            "name": "new circle 983"
        }
    }
    }
    """

def registerTest():
    api = '/register'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    the_same_phone = "159961"+str(random.randint(10000,99999))
    city = u"漳州"
    country = u"中国"
    state = u"福建"
    faculty = u"金融"
    major = u"经济管理"
    companny = "google China"
    admission_year = 2014
    job = "student"
    gender = 0
    password = "cxh1234567"
    name = "陈雄辉"
    # set request.
    dic[num] = {
        "city":city,
        "state":state,
        "country":country,
        "faculty":faculty,
        "name":name,
        "major":major,
        "company":companny,
        "admission_year":admission_year,
        "telephone":the_same_phone,
        "job":job,
        "gender":gender,
        "password":password
    }
    otherPara[num] = {}
    setMessage(message,num,"注册成功")
    num = num + 1
    #request.
    do_request(api,dic,message,"POST",otherPara)

def loginTest():
    api ='/login'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
        "password":"zp123455",
        "telephone":"15996198251"
    }
    otherPara[num] = {}
    setMessage(message,num,"密码错误")
    num = num + 1
    dic[num] = {
        "password":"cxh1234567",
        "telephone":"15996198251"
    }
    otherPara[num] = {}
    setMessage(message,num,"登陆成功")
    """
    num = num + 1
    dic[num] = {
        "password":"cxh1234567",
        "telephone":"15996198251"
    }
    otherPara[num] = {}
    setMessage(message,num,"重复登陆")
    num = num + 1
    dic[num] = {
        "password":"zp19950310",
        "telephone":"15996198251"
    }
    otherPara[num] = {}
    setMessage(message,num,"账号不存在")
    num = num + 1
    """
    do_request(api,dic,message,"POST",otherPara)

def logoutTest():
    api = "/logout"
    dic = {}
    otherPara = {}
    message = {}
    num = 0
    dic[num] = {}
    otherPara[num] = {}
    setMessage(message,num,"第1次退出账号")
    num = num + 1
    dic[num] = {}
    otherPara[num] = {}
    setMessage(message,num,"第2次退出账号")
    do_request(api,dic,message,"POST",otherPara)

def updateInfoTest():
    api = '/updateinfo'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
    }
    update_json = {
        "icon_url":"defauslts",        
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":0,
        "update_json":update_json
    }
    setMessage(message,num,"更新信息，icon_url 是 defaults")
    num += 1
    dic[num] = {
    }
    update_json = {
        "icon_url":"default",
        "job":"worker"+str(random.randint(1,120))     
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":1,
        "update_json":update_json
    }
    setMessage(message,num,"更新信息，icon_url 是 default，job 是 worker")
    num += 1
    dic[num] = {
    }
    update_json = {
        "icon_url":"default",
        "job":"worker"+str(random.randint(1,120)),
        "city":"321"      
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":0,
        "update_json":update_json
    }
    setMessage(message,num,"更新信息，icon_url 是 default，job 是 worker,city = 321")   
    num += 1
    dic[num] = {
    }
    update_json = {
        "icon_url":"default",
        "job":"worker"+str(random.randint(1,120)),
        "city":"321",
        "company":"another company"
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":0,
        "update_json":update_json
    }
    num+=1
    dic[num] = {
    }
    update_json = {
        "icon_url":"default",
        "introduction":"i change my introduction"+str(random.randint(1,120)),   
    }
    update_json = json.dumps(update_json)
    otherPara[num] = {
        "list_info_has_update":0,
        "update_json":update_json
    }
    setMessage(message,num,"更新信息，icon_url 是 defaults")
    setMessage(message,num,"更新信息，icon_url 是 default，job 是 worker,city = 321,company = another company")   
    do_request(api,dic,message,"POST",otherPara)

def editTest():
    api ='/edittopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
        "description":"changed!",
        "topic_id":"57bfa306ee78507903b49a06"
    }
    otherPara[num] = {}
    setMessage(message,num,"change description")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def detailTest():
    api = '/detailtopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
        "topic_id":"57c69d68d36ef3151eb80bac"
    }
    otherPara[num] = {}
    setMessage(message,num,"get topic detail")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def gettypetopicTest():
    api = '/gettypetopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
    "t_cat_id":"57bdcad0d0146385e6abb6be",
    "page":1,
    "count":2
    }
    otherPara[num] = {}
    setMessage(message,num,"get topic type")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def searchTopicTest():
    api = '/searchtopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    dic[num] = {
        "count":10,
        "q":"软院",
        "page":1
    }
    otherPara[num] = {}
    setMessage(message,num,"search topic")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)    

def createTopic():
    api = '/createTopic'
    num = 0
    dic = {}
    message = {}
    otherPara = {
    }
    dic[num] = {

    }
    otherPara[num] = {
        "circle_name":"new circle "+str(random.randint(1,1000)),
        "circle_icon_url":"default",
        "creator_uid":123,
        "circle_type_id":1,
        "circle_type_name":"学院圈",
        "reason_message":"I love you!",
        "description":" the circle will be beautiful!"
    }
    setMessage(message,num,"create topic")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)

def reviewListTest():
    api = "/reviewlisttopic"
    num = 0
    dic = {}
    message ={}
    otherPara = {}
    dic[num] = {}
    otherPara[num] ={
        "result":0,
        "since_id":1,
        "limit_num":5
    }
    setMessage(message,num,"review create topic list")
    num = num + 1
    do_request(api,dic,message,"GET",otherPara)

def reviewTest():
    api = "/reviewresult"
    num = 0
    dic = {}
    message ={}
    otherPara = {}
    dic[num] = {}
    otherPara[num] ={
        "result":1,
        "review_id":86,
    }
    setMessage(message,num,"review topic")
    num = num + 1
    do_request(api,dic,message,"POST",otherPara)


def adminRegister():
    api = '/adminregister'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    the_same_phone = "15195861108"
    city = 123
    faculty_id = 71
    major_id = 1
    companny = "google China"
    admission_year = 2014
    job = "student"
    gender = 0
    password = "123456"
    m = hashlib.md5()
    m.update(password)
    psw = m.hexdigest()    
    name = "陈雄辉"
    # set request.
    dic[num] = {
        "city":city,
        "faculty_id":faculty_id,
        "name":name,
        "major_id":major_id,
        "company":companny,
        "admission_year":admission_year,
        "telephone":the_same_phone,
        "job":job,
        "gender":gender,
        "password":psw
    }
    otherPara[num] = {}
    setMessage(message,num,"admin 注册成功")
    num = num + 1
    #request.
    do_request(api,dic,message,"POST",otherPara)    


def adminloginTest():
    api ='/login'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    password = "123456"
    m = hashlib.md5()
    m.update(password)
    psw = m.hexdigest()   
    dic[num] = {
        "password":psw,
        "telephone":"15195861108"
    }
    otherPara[num] = {}
    setMessage(message,num,"登陆成功")
    do_request(api,dic,message,"POST",otherPara)

def checkPhone():
    api = '/checkphone'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    password = "123456"
    m = hashlib.md5()
    m.update(password)
    psw = m.hexdigest()   
    dic[num] = {
    }
    otherPara[num] = {
        "telephone":"15195861108"
    }
    setMessage(message,num,"telephone has been register")
    do_request(api,dic,message,"POST",otherPara)    

# checkPhone()
# registerTest()    
loginTest()
# getcommentlist()
#getmessage()
#circle_member_list()
#user_detail()
#like()
#commit_list()
# pub_comment()
# search()
#follow_test()
# get_follow_list() 
# update_feed()
circle_feed_list()
# feed_detail()
# logoutTest()
# updateInfoTest()
# editTest()
# detailTest()
# searchTopicTest()
# gettypetopicTest()
# get_all_circle_test()
# createTopic()
# reviewListTest()
# reviewTest()    
#circle_apply_test()
#get_my_filter_circle_test()
# logoutTest()
"""
adminRegister()
adminloginTest()
"""
