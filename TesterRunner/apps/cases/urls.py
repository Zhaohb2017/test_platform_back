#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2019/3/4 15:09
@ file: urls.py
@ site: 
@ purpose: 
"""
from django.urls import path
from . import views

app_name = 'apps.cases'

urlpatterns = [
    path('c_add', views.AddCaseView),
    path('c_list', views.QueryByParams),
    path('search', views.QueryByName),
    path('c_del', views.DeleteView),
    path('c_edit', views.UpdateCase),
    path('run', views.RunView),
    path('r_list', views.QueryReport),
]
