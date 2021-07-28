# 导入之前安装的库
#中原地产https://tj.centanet.com
import re
import requests
from bs4 import BeautifulSoup

root_url = 'https://tj.centanet.com'
child_url = '/xiaoqu/xiqingqu/g1/'
init_url = root_url+child_url
cur_url = init_url

fo = open("big_house_ansi.txt", "w",)


xiaoqu_names=[]

while(1):
    r = requests.get(cur_url)
    r.encoding = 'utf-8'
    #r.encoding = 'ansi'
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    item_list = soup.find_all(class_='house-item clearfix')
    #print(item_list.__sizeof__())
    print("item length:",item_list.__len__())
    print("##########################")
    cnt = 0
    for item in item_list:
        #print(item)
        fo.write(item.contents[3].contents[1].contents[1].contents[0])
        fo.write(" ")
        fo.write(item.contents[3].contents[3].contents[6].split("\n                ")[1])
        fo.write("\n")


    url_list = soup.find_all(class_='fsm fb')
    next_page_found = False
    for url_temp in url_list:
        #print(url_temp)
        if(url_temp.contents[0]=="下一页"):#
            child_url = url_temp.attrs["href"]
            next_page_found=True

    cur_url = root_url+child_url
    if next_page_found==False:
        break


fo.close()