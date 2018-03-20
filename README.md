# job  接口
主要是 django rest-framework api的介绍

## 起因
看了一段时间的django-restframework 等一些框架，因此希望很好梳理一下。


## 实现

1. 爬取拉钩网的工作信息，
2. 根据爬取到的数据存入数据库
3. 写对应的api接口

## 运行方式
1. 安装对应的依赖包
> pip install -r requirement.txt
2. 更新所有的模块
> python manage.py migrate
3.运行环境（默认8000端口）
> python manage.py runserver
4. 爬取拉钩数据（注：本例数据已经存在db.sqllite中，所以此部可以略过）
入数据库中数据过于陈旧，也可在执行一次，爬取最新的数据：
触发方式,在浏览器中输入如下url:
> htttp://localhost:8000/excute

5. 查看对应的api,比如
> http://localhost:8000/job/rest/joblist?id=&city=武汉

## 运行效果如下：
![image](https://github.com/huangxifa/job/blob/master/jobfinder/django_rest_framework.png)

