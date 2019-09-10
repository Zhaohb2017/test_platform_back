from django.urls import path
from . import views

app_name = 'apps.versions'

urlpatterns = [
    path('versions_add', views.Add_Versions),
    path('versions_list', views.Query),
    path('search',  views.Search),
    path('del', views.DeleteView),



]
