from django.urls import path
from . import views

app_name = 'apps.testReport'

urlpatterns = [
    path('t_add',   views.Add_TestReport), #增加
    path('t_list',  views.Query),          #列表查询
    path('t_del',   views.Delete),         #数据删除
    path('search',  views.Search),         #搜索
    path('report', views.QueryReport),     #报告

    path('add_weekly',   views.Add_weekly), #周报
    path('list_weekly', views.QueryWeekly),
    path('del_weekly', views.WeeklyDelete),
    path('report_weekly', views.QueryWeekReport),
    path('search_weekly', views.WeekSearch),





]
