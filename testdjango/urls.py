"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from user import views
from django.urls import include  # 导入include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^$',views.pie_bar_test),
    re_path(r'^$',views.login),
    path('register', views.register),
    path('login', views.login),
    path('index/',views.index),
    path('ana/',views.ana),
    path('ciyun/', views.ciyun),
    path('updatepass', views.updatepass),
    path('zhexian/', views.zhexian),
    path('history/',views.history),
# path('<path:path>', views.catch_all, name='catch_all')



]
