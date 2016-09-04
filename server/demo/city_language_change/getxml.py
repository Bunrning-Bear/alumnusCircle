# getxml.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)   
sys.setdefaultencoding('utf-8')

from xml.dom.minidom import parse
import xml.dom.minidom
import json

tree = xml.dom.minidom.parse("simplelocation.xml")
collection = tree.documentElement
CountryRegion = collection.getElementsByTagName('CountryRegion')
city_list = []
country_list = []
state_list = []

for region in CountryRegion:
    if region.hasAttribute('Name'):
        print "country name is : %s its id is : %s"%(region.getAttribute('Name'),region.getAttribute('Code'))
        country_list.append(region.getAttribute('Name'))
        stateUnit = []
        State = region.getElementsByTagName('State')
        for state in State:
            if state.hasAttribute('Name'):
                print "     state is %s its id is %s"%(state.getAttribute('Name'),state.getAttribute('Code'))
                stateUnit.append(state.getAttribute('Name'))
                City = state.getElementsByTagName('City')
                cityUnit =[]
                for city in City:
                    if city.hasAttribute('Name'):
                        print " city is %s its id is %s"%(city.getAttribute('Name'),city.getAttribute('Code'))
                        cityUnit.append(city.getAttribute('Name'))
            else:
                city_list.append(cityUnit)

        state_list.append(stateUnit)



f = open("result.txt","w+"  )
# print >> f , country_list
#symptom= str(country_list).replace('u\'','\'')
#symptom.decode("unicode-escape")
#print symptom
jsonCountry = json.dumps(country_list,ensure_ascii=False)
jsonState = json.dumps(state_list,ensure_ascii=False)
jsonCity = json.dumps(city_list,ensure_ascii=False)
print >>f,"country_list=%s"%jsonCountry
print >>f,"state_list=%s"%jsonState
print >>f,"jsonCity=%s"%jsonCity
