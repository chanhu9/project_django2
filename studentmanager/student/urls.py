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

    url(r'^classes/(?P<value1>\d+)/(?P<value2>.+)/$', views.classes, name="班级信息"),

    url(r'^canshu/(?P<value1>\d+)/(?P<value2>.+)/$', views.canshu, name="参数"),

    url(r'^studentone/$', views.studentone, name="stu1"),

    url(r'^student2/$', views.student2, name="stu2"),

    url(r'^student3/$', views.student3, name="stu3"),

    url(r'^student4/$', views.student4, name="stu4"),

    url(r'^student5/$', views.student5, name="stu5"),

    url(r'^student6/$', views.student6, name="stu6"),

    url(r'^set_cookie/$', views.set_cookie, name="set_cookie"),

    url(r'^get_cookie/$', views.get_cookie, name="get_cookie"),

    url(r'^set_session/$', views.set_session, name="set_session"),

    url(r'^get_session/$', views.get_session, name="get_session"),

    url(r'^register/$', views.Register.as_view(), name="register"),

    url(r'^center/$', views.Center.as_view(), name="center"),

    url(r'^stuindex/$', views.Stuindex.as_view(), name='stuindex')

]

