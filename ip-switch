# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:18:02 2020

to identify the ip-switch

@author: kwang6
"""

from netmiko import ConnectHandler
import pandas as pd
from pandas import DataFrame
import re
from cisco import cisco

data = pd.read_excel(r'C:\Users\kwang6\Desktop\netmiko.xlsx')

##print(data.values)

maclist = list(data['mac'])
data['mac-ports'] = None
data['switch'] = None
data['mac-ports-original'] = None

a = ConnectHandler(**cisco)
a.find_prompt()



b = a.send_command('show mac address-table address '+maclist[1])
print(b)
timer = 0
for i in maclist:
    b = a.send_command('show mac address-table address '+ i)
    if 'dynamic' in b:
        data['mac-ports-original'][timer] = b
        text1 = re.compile(r'dynamic.+').findall(b)
        text2 = re.compile(r'Po.+').findall(text1[0])
        data['mac-ports'][timer] = text2[0]
        c = a.send_command('show int description | in '+ text2[0])
        data['switch'][timer] = c
        timer +=1

    else:
        data['mac-ports-original'][timer] = b
        data['mac-ports'][timer] = "no dympic"
        data['switch'][timer] = "no dympic"
        timer +=1


data.to_csv(r'C:\Users\kwang6\Desktop\wangkai\ip-switch.csv', encoding='utf-8-sig')




