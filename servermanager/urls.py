#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence 
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.org/
@software: PyCharm
@file: urls.py
@time: 2017/8/27 上午2:27
"""

# from django.urls import path
from django.conf.urls import include, url

from werobot.contrib.django import make_view
from .robot import robot

app_name = "servermanager"
urlpatterns = [
    url(r'robot', make_view(robot)),

]
