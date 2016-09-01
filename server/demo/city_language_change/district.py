#district.py

import MySQLdb
import urllib2
import json
import sys

reload(sys)   
sys.setdefaultencoding('utf-8')   

conn = MySQLdb.connect(host='localhost',user='root',passwd='zp19950310',db='world',charset='utf8')
cur = conn.cursor()
# cur.execute("SELECT COUNT(ID) FROM `City` WHERE CountryCode = 'CHN'")
cur.execute("SELECT Code FROM `Country`")
result = cur.fetchall()
for row in result: 
    Code = row[0]
    cur.execute("SELECT District FROM `City` WHERE CountryCode = \'"+str(Code)+'\'')
    for district_name in cur.fetchall():
        print "INSERT INTO `District` (district_name,CountryCode) VALUES ( \'"+str(district_name[0]) + "\' , \'"+str(Code)+"\' )"
        cur.execute("INSERT INTO `District` (district_name,CountryCode) VALUES ( \'"+str(district_name[0]) + "\' , \'"+str(Code)+"\' )")
        conn.commit()