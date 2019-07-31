#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2019/2/18 14:25
@ file: urls.py
@ site: 
@ purpose: 
"""

from django.urls import path
from . import views

app_name = 'apps.users'

urlpatterns = [
    path('u_add', views.UserAddView),
    path('u_list', views.UserQueryAllView),
]