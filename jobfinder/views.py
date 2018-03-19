from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from jobfinder.lagou.lagouspider import myspider


def excute(request):
    # spider = myspider("Python", "深圳")
    # from django import db
    # db.connections.close_all()
    print("a")
    job_type = ['java', 'python', 'php', 'go', '前端', 'ruby', '大数据']
    city_area = ['武汉', '北京', '上海', '广州', '深圳', '杭州']
    for job in job_type:
        for city in city_area:
            spider = myspider(job, city)
            spider.main()
    return HttpResponse("success")
