from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("index.html", views.index, name='home'),
    path("about.html", views.about, name='about'),
    path("shop.html", views.shop, name='shop'),
    path("blog.html", views.blog, name='blog'),
]
