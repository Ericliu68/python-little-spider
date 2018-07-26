# -*- coding: utf-8 -*-
"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from map import views as map_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 主页    localhost:8110/index/
    url(r'^index/', map_views.index),
    # 热力图
    url(r'^heat/', map_views.heat),
    # 散点图
    url(r'^scatter/', map_views.scatter),
    # 柱状图
    url(r'^histogram/', map_views.histogram),
    url(r'^form/',map_views.form),
    # post接收地址
    url(r'^data/', map_views.data),
    # 主页   localhost:8110   放到下面能用，不能放上去
    url(r'', map_views.index),
]
