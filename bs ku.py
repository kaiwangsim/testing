
from bs4 import BeautifulSoup
#爬取HTML要用BS库
import re
import requests

url1 = 'https://m.weibo.cn/detail/4515657263225384'
r1 = requests.get(url1)
soup = BeautifulSoup(r1.text,"html.parser")


script_content = soup.find_all("script")[1]


aa = re.compile(r'"text".+')

aa1 = re.compile(r'created_at.+')

aa2 = aa1.findall(script_content.text)

a1 = aa.findall(script_content.text)

x = a1[0]

pat=re.compile(r'[\u4e00-\u9fa5]+')
xx = pat.findall(x)



jj=''
for i in xx:
    jj = jj + i

print(jj)



b = 'Legend: \n        * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC\n        age - seconds since last seen,+ - primary entry using vPC Peer-Link\n   VLAN     MAC Address      Type      age     Secure NTFY   Ports/SWID.SSID.LID\n---------+-----------------+--------+---------+------+----+------------------\n* 300      2c54.2dc9.7841    dynamic   10         F    F  Po46\n'


c=re.compile(r'\n.+').findall(b)