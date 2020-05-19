# -*- coding: utf-8 -*-
# author: songwei
# place: Shenzhen Guangdong
# time: 2020/5/18 9:31
import os, re, json, traceback
import requests
from bs4 import BeautifulSoup
import time
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

# 开始时间
t1 = time.time()
print('#' * 50)

disease_list=[]
info_list=[]
cause_list=[]
prevent_lst = []
neopathy_list= []
symptom_list = []
inspect_list = []
diagnosis_list = []
treat_list= []
nursing_list = []
food_list = []
all_result=[]


def get_url_list(num):
    url_all_list=[]
    for i in range(1,num+1):
        url_list=[]
        url="http://jib.xywy.com/il_sii/gaishu/%s.htm" %i
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                                                 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }
        req=requests.get(url,headers=headers)
        soup=BeautifulSoup(req.text.encode(req.encoding), "lxml")
        if soup:
            url_find=soup.find_all("ul", class_="jib-nav-list clearfix")
            for i in url_find:
                for j in i.find_all("a"):
                    url_list.append("http://jib.xywy.com"+j["href"])
        url_all_list.append(url_list)
    return url_all_list



def parse(url_List):
    result=[]
    req=requests.get(url_List[0])
    disease_soup=BeautifulSoup(req.text.encode(req.encoding), "lxml")
    disease_find=disease_soup.find("div", class_="jib-articl-con jib-lh-articl")
    disease=disease_find.find("strong", class_="db f20 fYaHei fb jib-articl-tit tc pr").text.split("简介")[0]
    info=disease_find.find_all("p")[0].text
    # disease_list.append(disease)
    # info_list.append(info)
    result.append(disease)
    result.append(info)
    for i in url_List[1:]:
        # print(i)
        other_req=requests.get(i)
        other_soup=BeautifulSoup(other_req.text.encode(other_req.encoding).decode('gbk'), "lxml")
        other_result=other_soup.find_all("ul", class_="jib-nav-list clearfix")
        p_result = other_soup.find_all("div", class_="jib-articl fr f14 jib-lh-articl")
        p_all_result= other_soup.find_all("div", class_=" jib-articl fr f14 jib-lh-articl")
        # print(p_result)
        result_text = ""
        for i in p_result+p_all_result:
            result_text += i.text
            # print(result_text)
        result.append(result_text)
    # print(result)
    all_result.append(result)

    return all_result

if __name__ == '__main__':
    start=time.time()
    end=10
    p=get_url_list(end)
    # all_result=[]
    all_result=list(map(lambda x:parse(x),p))
    end=time.time()
    print(end-start)

    print(all_result)
































