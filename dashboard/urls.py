# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
