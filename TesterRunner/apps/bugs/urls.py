#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2019/2/28 14:04
@ file: urls.py
@ site: 
@ purpose: 
"""
from django.urls import path
from . import views

app_name = 'apps.bugs'

urlpatterns = [
    path('b_add', views.AddBug),
    path('b_list', views.QueryBug),
    path('b_del', views.DeleteBug),
    path('b_edit', views.UpdateBug),
    path('search', views.QueryByName),
]