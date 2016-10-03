# delete_databases.py
#Author ChenXionghui


import urllib2
import urllib
import cookielib
import json
import random
import hashlib

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
info_json = json.dumps(dic[count])
para = otherPara[count]
para['info_json'] = info_json
# print "do request :" + str(para) + str(ot)
req = set_resquest(api,para,method)
response = urllib2.urlopen(req)
the_page = response.read()
print message[count] + the_page
count = count + 1   