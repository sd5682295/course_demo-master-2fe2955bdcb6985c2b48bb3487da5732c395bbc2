# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-03-18 09:34:48
# @Last Modified by:   Anderson
# @Last Modified time: 2018-03-23 20:44:20
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('blog/<slug:blog_link>/', views.blog_detail,name='blog_detail')
]
