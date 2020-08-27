# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:48:49 2020

@author: wangkai
"""

from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler
import pandas as pd
import re

remote_device = {
    'device_type': 'autodetect',
    'host': '192.168.1.1',
    'username': 'user',
    'password': 'pass',
}


guesser = SSHDetect(**remote_device)
best_match = guesser.autodetect()
print('Firmware Type:', best_match)

remote_device['device_type'] = best_match
connection = ConnectHandler(**remote_device)

vlan_set = connection.send_command('show ip interface brief', use_textfsm=True)

svi_list = []

for i in vlan_set:
    if 'Vlan' in i['intf']:
        svi_list.append(i['intf'])

list1 = []
list2 = []
for svi in svi_list:
    ipadd = connection.send_command('show running-config interface {} | in address | exclude dhcp'.format(svi))
    dhcpadd = connection.send_command('show running-config interface {} | include dhcp'.format(svi))
    #if nxos
    if remote_device['device_type'] == 'cisco_nxos' and 'ip dhcp relay address' in dhcpadd:
        list1.append(svi)
        ipadd = re.compile(r'10.+').findall(ipadd)
        ipadd = ipadd[0]
        list1.append(ipadd)
        dhcpadd=re.compile(r'10.+?(?=\s)').findall(dhcpadd)
        for i in dhcpadd:
            list1.append(i)
        list2.append(list1)
        list1=[]


df=pd.DataFrame(list2, columns=['vlan', 'ip', 'dhcp1','dhcp2','dhcp3'])

df.to_csv(r'C:\Users\kwang6\Desktop\wangkai\dhcp.csv', encoding='utf-8-sig')    


new_dhcp = '10.194.102.54'

lista=[]
listb=[]
timer=0
timer1=0
for i in df['dhcp2']:
    if new_dhcp != i:
        timer1+=1
        lista.append(df['vlan'][timer])
        lista.append(df['dhcp2'][timer])
        listb.append(lista)
        lista=[]
        timer+=1
    else:
        timer+=1
        continue
df1=pd.DataFrame(listb, columns=['vlan', 'dhcp2'])

a = len(df['dhcp2'])

print(f'{timer1} out {a} is mismatch, as below:\n\n\n', df1)






    