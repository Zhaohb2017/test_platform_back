from django.urls import path
from . import views

app_name = 'apps.addcard'

urlpatterns = [
    path('c_add', views.Add_Card),
    path('c_list', views.QueryAllCard),
    path('search', views.Search),
    path('c_del', views.DeleteView),
    path('send_room', views.putCardInTheRoom),

]
