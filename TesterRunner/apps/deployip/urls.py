from django.urls import path
from . import views

app_name = 'apps.deployip'

urlpatterns = [
    path('i_add', views.AddDeployIP),
    path('i_list', views.QueryList),
    path('i_del', views.DeleteView),
    path('search', views.Search),
    path('send', views.Send),



]
