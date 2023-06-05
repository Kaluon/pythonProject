import requests
from pyquery import PyQuery
import csv
import time
import database

#浏览器的请求头
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
base_url='https://book.dangdang.com/'
#获取页面
res=requests.get(base_url,headers=headers)
#解析界面
html=res.content.decode('GBK')

doc=PyQuery(html)
for i in range(4,8):
    book_ul=doc('#mapid_7969791_parent_5298_part_ #component_7969791__5298_529%d__529%d li'%(i,i)).items()
    for one_li in book_ul:
        # print(one_li)
        img_url = one_li('img').attr('src')
        # print(img_url)
        title=one_li('.name a').attr('title')
        # print(title)
        price=one_li('.price .rob').text()
        # print(price)
        tuple_imformation=tuple([img_url,title,price])
        # print(tuple_imformation)
        database.insert_imformation(tuple_imformation)


