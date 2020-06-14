# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:09:35 2020

@author: Wang Kai
"""
import requests
import pandas as pd


url = r'https://m.weibo.cn/api/container/getIndex?uid=2803301701&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5&type=uid&value=2803301701&containerid=1076032803301701'

a = requests.get(url).json().get('data').get('cards')   #一个URL里面所有的微博

list1 = []
list2 = []
for i in range(1, len(a)):  #遍历一个URL（下滚动作）里面的所有微博，存入list2
    c = a[i]['mblog']  #单条微博
    list1.append(c.get('created_at'))
    list1.append(str(c.get('reposts_count')))
    list1.append(str(c.get('comments_count')))
    list1.append(str(c.get('attitudes_count')))
    list1.append('https://m.weibo.cn/detail/' + str(c.get('id')))
    list1.append(c.get('text'))
    list2.append(list1)
    list1=[]
    

since1 = requests.get(url).json().get('data').get("cardlistInfo").get("since_id")
url1 = url + "&since_id=" + str(since1)  #第一个URL

t = 10
urlx = url1
while t:
    sincex = requests.get(urlx).json().get('data').get("cardlistInfo").get("since_id")
    urlx = url + "&since_id=" + str(sincex)  #第N个URL
    t-=1
    ai = requests.get(urlx).json().get('data').get('cards')
    for i in range(1, len(ai)):  #遍历一个URL（下滚动作）里面的所有微博，存入list2
        c = ai[i]['mblog']  #单条微博
        list1.append(c.get('created_at'))
        list1.append(str(c.get('reposts_count')))
        list1.append(str(c.get('comments_count')))
        list1.append(str(c.get('attitudes_count')))
        list1.append('https://m.weibo.cn/detail/' + str(c.get('id')))
        list1.append(c.get('text'))
        list2.append(list1)
        list1=[]

df = pd.DataFrame(list2, columns=['创建时间','转发数','评论数','点赞数','原文链接','内容'])
df.to_csv(r'C:\Users\Wang Kai\Desktop\my.csv', encoding='utf-8-sig')


