#urllibtest.py
import urllib2
import urllib
import cookielib
import json
prefix = "http://localhost:8000"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
resp = urllib2.urlopen(prefix+'/')

def set_resquest(api,data,method):
    # data is json.
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

api ='/login'
info_json = {
    "user_passwd":"zp19950310",
    "user_phone":"15196197203"
}
info_json = json.dumps(info_json)
para = {
    "info_json":info_json
}
req = set_resquest(api,para,"POST")
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
response = urllib2.urlopen(req)
the_page = response.read()
print the_page