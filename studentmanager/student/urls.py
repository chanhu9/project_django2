#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/27 14:42

from django.conf.urls import url, include

# from student.views import studentsAll
from student import views





urlpatterns = [
    url(r'^student/all/$', views.studentAll, name="所有学生"),

    url(r'^subject/(\d+)/(.+)/$', views.subject, name="subject"),

    url(r'^get_path/$', views.get_path, name="获取路径"),

    url(r'^classes/(?P<value2>\d+)/(?P<value1>.+)/$', views.classes, name="班级信息"),

    url(r'^canshu/(?P<value2>\d+)/(?P<value1>.+)/$', views.canshu, name="参数"),

]

