# -*- coding: utf-8 -*-
# author: songwei
# place: Shenzhen Guangdong
# time: 2020/5/14 16:47
import os, re, json, traceback


import requests
from bs4 import BeautifulSoup


class spider:
    def __init__(self):
        self.base_url="http://jib.xywy.com/"
        self.result={}
        self.result["disease"]=[]
        self.result["info"]=[]
        self.result["prevent"]=[]
        self.result["neopathy"]=[]
        self.result["symptom"]=[]
        self.result["inspect"] = []
        self.result["diagnosis"] = []
        self.result["treat"] = []
        self.result["nursing"] = []
        self.result["food"] = []
        return

    def connect_info(self):
        begin=1
        end=100
        for num in range(begin,end):
            info_url=self.base_url+"/il_sii/gaishu/{}.htm".format(num)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                                                     (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
            }

            req = requests.get(info_url, headers=headers)
            if req.status_code == 200:
                soup = BeautifulSoup(req.text.encode(req.encoding), "lxml")
                soup1 = soup.find("div", class_="jib-articl-con jib-lh-articl")
                print(soup)
                if soup1:

                    disease = soup1.find("strong", class_="db f20 fYaHei fb jib-articl-tit tc pr").text.split("简介")[0]
                    info = soup1.find_all("p")[0].text
                    self.result["disease"].append(disease)
                    self.result["info"].append(info)

                    urlSoup=soup.find_all("ul", class_="jib-nav-list clearfix")
                    urlList=[]
                    if urlSoup:
                        for i in urlSoup:
                            for j in i.find_all("a"):
                                urlList.append(j["href"])
                    print(urlList)

                    def get_result(k):
                        nextReq = requests.get(self.base_url + k, headers=headers)
                        nextSoup = BeautifulSoup(nextReq.text.encode(nextReq.encoding), "lxml")
                        p_result=nextSoup.find_all("div",class_="jib-articl fr f14 jib-lh-articl")
                        result_text=""
                        for i in p_result:
                            result_text+=i.text
                        return result_text

                    data=list(map(lambda x:get_result(x),urlList[1:]))
                    self.result["food"].append(data.pop())
                    self.result["nursing"].append(data.pop())
                    self.result["treat"].append(data.pop())
                    self.result["diagnosis"].append(data.pop())
                    self.result["inspect"].append(data.pop())
                    self.result["symptom"].append(data.pop())
                    self.result["neopathy"].append(data.pop())
                    self.result["prevent"].append(data.pop())
        return self.result

a=spider()
print(a.connect_info())

























































