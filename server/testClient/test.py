# -*- coding: utf8 -*-  
# code by Shurrik  
import threading, time, httplib 
import urllib2
import urllib
import cookielib
import json
import random
import hashlib 
prefix ="http://139.196.207.155:8000"
HOST = "http://139.196.207.155"; #主机地址 例如192.168.1.101  
PORT = 8000 #端口  
URI = "login" #相对地址,加参数防止缓存，否则可能会返回304  
TOTAL = 0 #总数  
SUCC = 0 #响应成功数  
FAIL = 0 #响应失败数  
EXCEPT = 0 #响应异常数  
MAXTIME=0 #最大响应时间  
MINTIME=100 #最小响应时间，初始值为100秒  
GT3=0 #统计3秒内响应的  
LT3=0 #统计大于3秒响应的  
# 创建一个 threading.Thread 的派生类  

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

def setMessage(message,content):
   message = content + "\r\n"

def set_info_json(dic):
    info_json = json.dumps

def do_request(api,dic,message,method,otherPara):
    count = 0
    info_json = json.dumps(dic)
    para = otherPara
    para['info_json'] = info_json
    # print "do request :" + str(para) + str(ot)
    req = set_resquest(api,para,method)
    response = urllib2.urlopen(req)
    return response


api ='/login'
num = 0
info_json = {}
message = {}
otherPara = {}
# info_json[num] = {
#     "password":"xcf324",
#     "telephone":"15689236999"
# }
# otherPara[num] = {}
# setMessage(message,num,"密码错误")
# num = num + 1
st = time.time()
info_json= {
    "password":"llf123456",
    "telephone":"15888888888"
}
num = num + 1
resp = do_request(api,info_json,message,"POST",otherPara)


class RequestThread(threading.Thread):  
    # 构造函数  
    def __init__(self, thread_name):  
        threading.Thread.__init__(self)  
        self.test_count = 0  
  
    # 线程运行的入口函数  
    def run(self):  
  
        self.test_performace()  
  
  
    def test_performace(self):  
            global TOTAL  
            global SUCC  
            global FAIL  
            global EXCEPT  
            global GT3  
            global LT3  
            try:  
                # st = time.time()  
                # conn = httplib.HTTPConnection(HOST, PORT, False)    
                # conn.request('GET', URI)  
                # res = conn.getresponse()    
                #print 'version:', res.version    
                #print 'reason:', res.reason    
                #print 'status:', res.status    
                #print 'msg:', res.msg    
                #print 'headers:', res.getheaders()  
                api='/search_user'
                num = 0
                info_json = {}
                message = {}
                otherPara = {}
                otherPara = {
                    "filter_admission_year_min":0,# 0 for not filter
                    "filter_admission_year_max":9999,# 9999 for not filter
                    "filter_major_list":json.dumps([u'_金融_',u'_软件学院_']),#([u'_金融_',u'_软件学院_']), # [] for not filter
                    "filter_city_list": json.dumps([]), # ([u'_中国_福建_漳州_']), # [] for not filter 
                    "all_match":0,# 0 for not query search. 1 for query search ,2 to get all people
                    "query":""
                }
                info_json = {
                }
                message = "search,\n"    
                do_request(api,info_json,message,"POST",otherPara)     
                start_time
                if resp.getcode() == 200:  
                    TOTAL+=1  
                    SUCC+=1  
                else:  
                    TOTAL+=1  
                    FAIL+=1  
                time_span = time.time()-st  
                print '%s:%f\n'%(self.name,time_span)  
                self.maxtime(time_span)  
                self.mintime(time_span)  
                if time_span>3:  
                    GT3+=1  
                else:  
                    LT3+=1                      
            except Exception,e:  
                print e  
                TOTAL+=1  
                EXCEPT+=1  
    def maxtime(self,ts):  
            global MAXTIME  
            print ts  
            if ts>MAXTIME:  
                MAXTIME=ts  
    def mintime(self,ts):  
            global MINTIME  
            if ts<MINTIME:  
                MINTIME=ts  
          
# main 代码开始  
print '===========task start==========='  
# 开始的时间  
start_time = time.time()  
# 并发的线程数  
thread_count = 300  
  
i = 0  
while i <= thread_count:  
    t = RequestThread("thread" + str(i))  
    t.start()  
    i += 1  
t=0  
#并发数所有都完成或大于50秒就结束  
while TOTAL<thread_count|t>50:  
        print "total:%d,succ:%d,fail:%d,except:%d\n"%(TOTAL,SUCC,FAIL,EXCEPT)  
        print HOST,URI  
        t+=1  
        time.sleep(1)  
print '===========task end==========='  
print "total:%d,succ:%d,fail:%d,except:%d"%(TOTAL,SUCC,FAIL,EXCEPT)  
print 'response maxtime:',MAXTIME  
print 'response mintime',MINTIME  
print 'great than 3 seconds:%d,percent:%0.2f'%(GT3,float(GT3)/TOTAL)  
print 'less than 3 seconds:%d,percent:%0.2f'%(LT3,float(LT3)/TOTAL)  