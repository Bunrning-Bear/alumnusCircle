#encoding=utf-8
# main.py
import MySQLdb
import urllib2
import json
import sys

# translate english into chinese by youdao dictory

reload(sys)   
sys.setdefaultencoding('utf-8')   
conn = MySQLdb.connect(host='localhost',user='root',passwd='zp19950310',db='world',charset='utf8')
cur = conn.cursor()
# cur.execute("SELECT COUNT(ID) FROM `City` WHERE CountryCode = 'CHN'")
cur.execute("SELECT * FROM `City` WHERE CountryCode = 'CHN' AND ID >=2248")
for row in cur.fetchall(): 
    ID = row[0]     
    Name =  row[1]
    District = row[3]
    resp1 = urllib2.urlopen("http://fanyi.youdao.com/openapi.do?keyfrom=alumnusCIrcle&key=397320889&type=data&doctype=json&version=1.1&q="+Name+"&only=translation")
    resp2 = urllib2.urlopen("http://fanyi.youdao.com/openapi.do?keyfrom=alumnusCIrcle&key=397320889&type=data&doctype=json&version=1.1&q="+District+"&only=translation")

    name_body = json.loads(resp1.read())
    district_body =json.loads(resp2.read())
    print Name,District
    if name_body['errorCode']!= 30 and district_body['errorCode'] !=30:
        name_change = name_body['translation'][0]
        district_change = district_body['translation'][0]
        cur.execute("UPDATE `City` set Name = \'" + name_change + "\', District = \'" + district_change + "\' WHERE ID = "+str(ID))
        print "UPDATE `City` set Name = \'" + name_change + "\', District = \'" + district_change + "\' WHERE ID = "+str(ID)
        conn.commit()
    
cur.close()
conn.close()