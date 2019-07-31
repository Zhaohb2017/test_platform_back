"""TesterRunner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import apps.users.views as users
from django.conf.urls.static import static
from . import settings


router = DefaultRouter()

urlpatterns = [
    path('index/', users.index),
    path('admin/', admin.site.urls),
    path('login', users.LoginView),
    path('register', users.UserAddView),
    path('logout', users.LogoutView),
    path('users/', include('apps.users.urls', namespace='apps.users')),
    path('bugs/', include('apps.bugs.urls', namespace='apps.bugs')),
    path('cases/', include('apps.cases.urls', namespace='apps.cases')),
    path('knowledge/', include('apps.knowledge.urls', namespace='apps.knowledge')),
    path('addcard/', include('apps.addcard.urls', namespace='apps.addcard')),
    path('deployip/', include('apps.deployip.urls', namespace='apps.deployip')),

]

urlpatterns += static('/report/', document_root=settings.STATIC_ROOT)
urlpatterns += static('/img/', document_root=settings.STATIC_ROOT)
