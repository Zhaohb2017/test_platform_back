from django.urls import path
from . import views

app_name = 'apps.log'

urlpatterns = [
    path('search',  views.Search),         #搜索
]
