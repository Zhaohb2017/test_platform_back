from django.urls import path
from . import views

app_name = 'apps.knowledge'

urlpatterns = [
    path('k_add', views.AddCasePoint),
    path('k_list', views.QueryTestPoint),
    path('k_update', views.UpdateTestPoint),
    path('k_search', views.SearchTestPoint),

    path('k_del', views.DeleteTestPoint),        #删除测试点
    path('add_case', views.AddTestCase),         #添加测试用例
    path('case_list', views.QueryTestCase),      #测试用例列表
    path('case_delete', views.DeleteCase),       #删除测试用例
    path('case_update', views.UpdateTestCase),   #更新测试用例
    path('case_search', views.SearchTestCase),   #搜索测试用例
    path('excel_data', views.BatchProduce),      #批量生成
    path('page_delete', views.PageDelete),        #删除当前页面全部数据



    path('s_add', views.AddKnowledge),
    path('s_list', views.QueryKnowledge),
    path('s_del', views.DeleteView),
    path('s_search', views.Searchskill),
    path('s_edit', views.UpdateSkill),

]
