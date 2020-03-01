import requests

url = 'https://vp.fact.qq.com/loadmore?artnum=0&page=0'

html = requests.get(url)
data = html.json()['content']

page = 0

content = True

data = []
while content:
    url1 = url + str(page)
    html = requests.get(url1)
    content = html.json()['content']
    data.extend(content)
    page+=1

print(f'total page is {page}')



import pandas as pd

df = pd.DataFrame(data)
df.to_csv(r'C:\Users\username\Desktop\较真.csv', encoding ='utf-8-sig')

