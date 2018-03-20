# -*- coding:utf-8 -*-
# date:2017-7-11
# anthor:hxf

import requests
import json
from urllib.parse import quote
from bs4 import BeautifulSoup

from jobfinder.lagou.config import myheaders
from jobfinder.models import JobList


class myspider(object):
    def __init__(self, mykey, mycity):
        # 自定义一个变量self.i，代表Excel表格的行数
        self.i = 1
        self.key = mykey
        self.city = mycity
        # 获取自定义请求头
        self.headers = myheaders.get_headers(mykey, mycity)
        # 获取表格类
        self.excel = myexcel(mykey, mycity)

    # 请求源代码，获取总页码数
    def get_pages(self):
        url = "https://www.lagou.com/jobs/list_{}?city={}&cl=false&fromSearch=true&labelWords=&suginput=".format(
            self.key, self.city)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"}
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, "html")
        totalnum = int(soup.select("span.totalNum")[0].text.strip())
        return totalnum

    # 获取单个页面的信息
    def get_one_html(self, pagenum):
        url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false".format(
            quote(self.city))
        data = {
            "first": "true",
            "pn": pagenum,
            "kd": self.key
        }
        html = requests.post(url=url, headers=self.headers, data=data).text
        infos = json.loads(html)
        jobs = infos["content"]["positionResult"]["result"]
        for data in jobs:
            lis = data["companyLabelList"]
            if len(lis) > 0:
                s = ",".join(lis)
            else:
                s = "None"
            link = "https://www.lagou.com/jobs/{}.html".format(data["positionId"])
            job = JobList(
                city=data["city"]
                , job=data["positionName"]
                , company=data["companyFullName"]
                , salary=data["salary"]
                , experience=data["workYear"]
                , education=data["education"]
                , area=data["district"]
                , scale=data["companySize"]
                , attraction=s
                , finacing=data["financeStage"]
                , pubdate=data["createTime"]
                , url=link
            )
            job.save()

    # 循环获取所有页面的信息
    def main(self):
        nums = self.get_pages()
        for n in range(1, nums + 1):
            self.get_one_html(n)
            print("总计{}页职位信息，已经成功写入{}页的信息到数据库".format(nums, n))
        print("该品类所有信息保存完毕！")
