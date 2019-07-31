from django.urls import path
from . import views

app_name = 'apps.knowledge'

urlpatterns = [
    path('k_add', views.AddCasePoint),
    path('k_list', views.QueryTestPoint),
    path('k_del', views.DeleteTestPoint),  #删除测试点
    
    path('s_add', views.AddKnowledge),
    path('s_list', views.QueryKnowledge),
    path('s_del', views.DeleteView),
    path('s_search', views.Searchskill),
    path('s_edit', views.UpdateSkill),

]
