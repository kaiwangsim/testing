
from bs4 import BeautifulSoup
#爬取HTML要用BS库
import re
import requests

url1 = 'https://m.weibo.cn/detail/4515667271909478'
r1 = requests.get(url1)
soup = BeautifulSoup(r1.text,"html.parser")

pattern = re.compile(r"var _url = '(.*?)';$", re.MULTILINE | re.DOTALL)
script = soup.find("script", text=pattern)