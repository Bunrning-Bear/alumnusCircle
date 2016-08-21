#urllibtest.py
# coding=utf-8
import urllib2
import urllib
import cookielib
import json
import random
prefix = "http://localhost:8000"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
# get _xrsf
resp = urllib2.urlopen(prefix+'/')
the_page = resp.read()
print the_page

_xsrf = json.loads(json.loads(the_page)['Data'])['_xsrf']

def set_resquest(api,data,method):
    # data is dictory.
    # method can be get put delete post ?
    # get _xsrf
    for item in cj:
        if item.name == '_xsrf':
            _xsrf = item.value    
    data['_xsrf'] = _xsrf
    data = urllib.urlencode(data)
    url = prefix + api
    request = urllib2.Request(url,data)
    request.get_method = lambda: method # or 'DELETE' 
    return request
def setMessage(message,num,content):
   message[num] = "No.%s"%num + content  
def set_info_json(dic):
    info_json = json.dumps
def do_request(api,dic,message,method,otherPara):
    count = 0
    while count < len(dic):
        info_json = json.dumps(dic[count])
        para = otherPara[count]
        para['info_json'] = info_json
        req = set_resquest(api,para,method)
        response = urllib2.urlopen(req)
        the_page = response.read()
        print message[count] + the_page
        count = count + 1    

def registerTest():
    api = '/register'
    num = 0
    dic = {}
    message = {}
    otherPara = {}
    the_same_phone = "151961"+str(random.randint(10000,99999))
    city = 123
    faculty_id = 71
    major_id = 1
    companny = "google China"
    admission_year = 2014
    job = "student"
    gender = 0
    password = "cxh1234567"
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
        "password":password
    }
    otherPara[num] = {}
    setMessage(message,num,"注册成功")
    num = num + 1
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
        "password":password
    }
    otherPara[num] = {}
    setMessage(message,num,"重复注册实例")
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
        "telephone":"15105861442"
    }
    otherPara[num] = {}
    setMessage(message,num,"密码错误")
    num = num + 1
    dic[num] = {
        "password":"zp19950310",
        "telephone":"15105861442"
    }
    otherPara[num] = {}
    setMessage(message,num,"登陆成功")
    num = num + 1
    dic[num] = {
        "password":"zp19950310",
        "telephone":"15105861442"
    }
    otherPara[num] = {}
    setMessage(message,num,"重复登陆")
    num = num + 1
    dic[num] = {
        "password":"zp19950310",
        "telephone":"15125861442"
    }
    otherPara[num] = {}
    setMessage(message,num,"账号不存在")
    num = num + 1
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
    otherPara[num] = {
        "icon_url":"default",
        "list_info_has_update":0
    }
    setMessage(message,num,"更新信息，icon_url 是 default")
    do_request(api,dic,message,"POST",otherPara)
registerTest()    
loginTest()
# logoutTest()
updateInfoTest()