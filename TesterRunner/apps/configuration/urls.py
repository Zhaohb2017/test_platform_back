from django.urls import path
from . import views

app_name = 'apps.configuration'

urlpatterns = [
    path('cfg_add', views.Addcfg),
    path('cfg_list', views.QueryList),

]
