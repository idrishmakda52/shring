from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage2,name="home2"),
    path('data/',views.homepage,name="home"),

    path('insert/',views.insert,name="insert"),
    path('retrive/',views.retrive,name="try")
  ]