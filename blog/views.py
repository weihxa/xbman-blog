#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'weihaoxuan'
from django.shortcuts import render
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template.context import RequestContext
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Q
import models
import utils
# Create your views here.


def index(request):
    articles = models.Article.objects.filter(status=0).order_by('-created_time')
    page = request.GET.get('page', 1)
    tag = request.GET.get('tag')
    categories = request.GET.get('category')
    seriess = request.GET.get('series')
    if tag:
        T = models.Tag.objects.get(name=tag)
        articles = articles.filter(tag=T)
    if categories:
        C = models.Categories.objects.get(name=categories)
        articles = articles.filter(categories=C)
    if seriess:
        S = models.Series.objects.get(name=seriess)
        articles = articles.filter(series=S)
    paginator = Paginator(articles, 10, request=request)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    tags = models.Tag.objects.all()
    links = models.Link.objects.all()
    categories = models.Categories.objects.all()
    series = models.Series.objects.all()
    return render(request, 'index.html',{'articles': articles,'links': links,'tags': tags,
                                         'categories': categories,'series':series,
                                         'theme':utils.setsession(request)},
                  context_instance=RequestContext(request))

def as_view(request,article_url):
    article = models.Article.objects.get(id=article_url)
    article.read += 1
    article.save()
    url = 'http://' + request.get_host() + request.get_full_path()
    series = models.Series.objects.all()
    return render(request, 'article.html',{'article': article,"url":url,'series':series,'theme':utils.setsession(request)},
                  context_instance=RequestContext(request))


def about(request):
    try:
        article_body = models.Setting.objects.get().body
    except Exception:
        article_body = u'####博主很懒什么都没留下:tw-1f33f:！'
    series = models.Series.objects.all()
    return render(request, 'about.html', {'body': article_body,'series':series,'theme':utils.setsession(request)},
                  context_instance=RequestContext(request))