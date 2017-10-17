"""xbmanblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
import views

urlpatterns = [
    url(r'^$', views.index,name='admin'),
    url(r'^login/$', views.login,name='login'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^checkpasswork/', views.checkpasswork,name='adcheckpasswork'),
    url(r'^create_code/$',views.create_code_img,name='create_code'),
    url(r'^index/$', views.index,name='adindex'),
    url(r'^addarticle/$', views.addarticle,name='addarticle'),
    url(r'^upload/$', csrf_exempt(views.upload),name='upload'),
    url(r'^addcategories/$', views.addcategories,name='addcategories'),
    url(r'^addtags/$', views.addtags,name='addtags'),
    url(r'^articlelist/', views.articlelist,name='articlelist'),
    url(r'^delarticle/', views.delarticle,name='delarticle'),
    url(r'^editarticle/', views.editarticle,name='editarticle'),
    url(r'^getarticleid/', views.getarticleid,name='getarticleid'),
    url(r'^link/', views.link,name='link'),
    url(r'^delink/', views.delink,name='delink'),
    url(r'^adminabout/', views.adminabout,name='adminabout'),
    url(r'^getabout/', views.getabout,name='getabout'),
    url(r'^addseries/$', views.addseries, name='addseries'),
    url(r'^adminweixin/$', views.adminweixin, name='adminweixin'),
    url(r'^delwkey/', views.delwkey, name='delwkey'),
    url(r'^wxreply/', views.wxreply, name='wxreply'),
    url(r'^delreply/', views.delreply, name='delreply'),
    url(r'^wxinstruction/', views.wxinstruction, name='wxinstruction'),
    url(r'^delinstruction/', views.delinstruction, name='delinstruction'),

]
