from django.urls import path
from . import views

app_name = 'apps.club'

urlpatterns = [
    path('add_people', views.AddPeople),
]
