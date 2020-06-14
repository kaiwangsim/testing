
from bs4 import BeautifulSoup
#爬取HTML要用BS库
import re
import requests

url1 = 'https://m.weibo.cn/detail/4515667271909478'
r1 = requests.get(url1)
soup = BeautifulSoup(r1.text,"html.parser")

pattern = re.compile(r"var $render_data = '(.*?)';$", re.MULTILINE | re.DOTALL)
script = soup.find_all("script", text=pattern)

s1 = soup.find_all("script")

t = 2
for i in soup.find_all('script'):
    a = i
    t -=1
    if t == 0:
        break
    
    