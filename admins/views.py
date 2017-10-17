#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'weihaoxuan'
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib import auth
from django.utils import timezone
import django
from admins import models
from blog import models as blogmodels
import json
import check_code
from io import BytesIO

def create_code_img(request):
    #在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    img,code = check_code.create_code()
    request.session['check_code'] = code
    img.save(f,'PNG')
    return HttpResponse(f.getvalue())

def login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        code = request.POST.get('code', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.valid_end_time: #设置了end time
                if django.utils.timezone.now() > user.valid_begin_time and django.utils.timezone.now()  < user.valid_end_time:
                    auth.login(request,user)
                    request.session.set_expiry(600*30)
                    if code == request.session.get('check_code', 'error'):
                        return HttpResponseRedirect('/admins/index/')
                    else:
                        return render(request, 'admins/login.html', {'login_err': '您输入的验证码错误,请重新输入！'})
                else:
                    return render(request,'admins/login.html',{'login_err': 'User account is expired,please contact your IT guy for this!'})
            elif django.utils.timezone.now() > user.valid_begin_time:
                    auth.login(request,user)
                    request.session.set_expiry(600*30)
                    if code == request.session.get('check_code', 'error'):
                        return HttpResponseRedirect('/admins/index/')
                    else:
                        return render(request, 'admins/login.html', {'login_err': '您输入的验证码错误,请重新输入！'})
        else:
            return render(request,'admins/login.html',{'login_err': '您输入的用户名或密码错误,请重新输入！'})
    else:
        return render(request, 'admins/login.html')

@login_required(login_url='/admins/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/admins/login/")

@login_required(login_url='/admins/login/')
def checkpasswork(request):
    if request.method=='POST':
        try:
            oidpassword=request.POST.get('oldpassword')
            password=request.POST.get('password')
            user= auth.authenticate(username=str(request.user),password=oidpassword)
            user.set_password(password)
            user.save()
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/admins/index/")
            return HttpResponseRedirect("/admins/login/")
        except AttributeError,e:
            return HttpResponseRedirect("/admins/login/")

@login_required(login_url='/admins/login/')
def index(request):
    if request.method == 'GET':
        containerd = {}
        containerd['brticle'] = blogmodels.Article.objects.all().count()
        containerd['nobrticle'] = blogmodels.Article.objects.filter(status=1).count()
        containerd['link'] = blogmodels.Link.objects.all().count()
        return render(request, 'admins/index.html',{"containerd": containerd,},
                      context_instance=RequestContext(request))

@login_required(login_url='/admins/login/')
def addarticle(request):
    if request.method == 'GET':
        categories = blogmodels.Categories.objects.all().values('name')
        tags = blogmodels.Tag.objects.all().values('name')
        series = blogmodels.Series.objects.all()
        return render(request, 'admins/addarticle.html', {'categories': categories, 'tags': tags,'series':series},
                      context_instance=RequestContext(request))
    elif request.method == 'POST':
        d = dict(request.POST)
        title = d['title'][0]
        status = d['status'][0]
        editormd = d['editormd-markdown-doc'][0]
        description = editormd.split('---')[0]
        series = request.POST.get('series')
        try:
            tags = d['tags']
        except KeyError:
            tags = ''
        try:
            categories = d['categories']
        except KeyError:
            categories = ''
        try:
            aid = d['id'][0]
            article = blogmodels.Article.objects.get(pk=aid)
            article.title = title
            article.body = editormd
            article.status = status
            article.description = description
            exist_tag = d['exist_tag'][0].split(',')
            old_tag = article.get_tag().strip(',').split(',')
            tags = list(set(tags).difference(set(exist_tag)))
            delete_tag_list = list(set(old_tag).difference(set(exist_tag)))
            for dt in delete_tag_list:
                t = blogmodels.Tag.objects.get(name=dt)
                article.tag.remove(t)
            exist_categories = d['exist_categories'][0].split(',')
            old_categories = article.get_categories().strip(',').split(',')
            categories = list(set(categories).difference(set(exist_categories)))
            delete_categories_list = list(set(old_categories).difference(set(exist_categories)))
            for dc in delete_categories_list:
                t = blogmodels.Categories.objects.get(name=dc)
                article.categories.remove(t)
        except Exception,e:
            article = blogmodels.Article.objects.create(title=title, body=editormd, status=status,
                                             description=description)
            if status == 0:
                article.release_time = timezone.now()
        if tags:
            for tag in tags:
                t = blogmodels.Tag.objects.get(name=tag)
                article.tag.add(t)
        if categories:
            for categorie in categories:
                c = blogmodels.Categories.objects.get(name=categorie)
                article.categories.add(c)
        if series:
            c = blogmodels.Series.objects.get(id=series)
            article.series = c
        article.save()
        return HttpResponseRedirect("/admins/articlelist/")

@login_required(login_url='/admins/login/')
def upload(request, *args, **kwargs):
    files = request.FILES.get('editormd-image-file', None)
    if files:
        img = models.Images.objects.create(image=files)
        result = {'success': 1, 'message': 'OK',
                  'url': request.META['HTTP_ORIGIN'] + '/static/upload/' + str(img.image)}
    else:
        result = {'success': 0, 'message': '未获取到文件！'}
    return HttpResponse(json.dumps(result), content_type='application/json')

@login_required(login_url='/admins/login/')
def addcategories(request):
    if request.POST.get('categories'):
        blogmodels.Categories.objects.create(name=request.POST.get('categories'))
    return HttpResponseRedirect("/admins/addarticle/")


@login_required(login_url='/admins/login/')
def addtags(request):
    if request.POST.get('tags'):
        blogmodels.Tag.objects.create(name=request.POST.get('tags'))
    return HttpResponseRedirect("/admins/addarticle/")

@login_required(login_url='/admins/login/')
def articlelist(request):
    if request.method == 'GET':
        articles = blogmodels.Article.objects.all().order_by('-id')
        return render(request, 'admins/articlelist.html',{'articles':articles},
                      context_instance=RequestContext(request))


@login_required(login_url='/admins/login/')
def delarticle(request):
    if request.method == 'POST':
        blogmodels.Article.objects.get(id=request.POST.get('modify')).delete()
        return HttpResponse(json.dumps('true'))

@login_required(login_url='/admins/login/')
def editarticle(request):
    aid = request.GET.get('aid', '')
    if aid:
        article = blogmodels.Article.objects.get(pk=aid)
    else:
        article = blogmodels.Article.objects.all().last()
    categories = blogmodels.Categories.objects.all().values('name')
    tags = blogmodels.Tag.objects.all().values('name')
    exist_categories = article.get_categories().strip(',')
    exist_tag = article.get_tag().strip(',')
    return render(request, 'admins/editarticle.html', {
        'categories': categories,
        'tags': tags,
        'article': article,
        'exist_categories': exist_categories,
        'exist_tag': exist_tag
    })

@login_required(login_url='/admins/login/')
def getarticleid( request):
    aid = request.GET.get('aid')
    article_body = blogmodels.Article.objects.get(pk=aid).body
    return HttpResponse(article_body)

@login_required(login_url='/admins/login/')
def link(request):
    if request.method == 'GET':
        links = blogmodels.Link.objects.all().order_by('-add_time')
        return render(request, 'admins/link.html', {'links': links})
    if request.method == 'POST' and request.POST.get('urls'):
        blogmodels.Link.objects.create(name=request.POST.get('name'),url=request.POST.get('urls'),description=request.POST.get('Description'))
    return HttpResponseRedirect("/admins/link/")

@login_required(login_url='/admins/login/')
def delink(request):
    if request.method == 'POST':
        blogmodels.Link.objects.get(id=request.POST.get('modify')).delete()
        return HttpResponse(json.dumps('true'))

@login_required(login_url='/admins/login/')
def adminabout(request):
    if request.method == 'GET':
        return render(request, 'admins/editabout.html',
                    context_instance=RequestContext(request))
    elif request.method == 'POST':
        try:
            about = blogmodels.Setting.objects.get()
            about.body = request.POST.get('editormd-markdown-doc')
            about.save()
        except Exception:
            blogmodels.Setting.objects.create(body=request.POST.get('editormd-markdown-doc')).save()
        return HttpResponseRedirect("/admins/adminabout/")

@login_required(login_url='/admins/login/')
def getabout(request):
    try:
        article_body = blogmodels.Setting.objects.get().body
    except Exception:
        article_body=''
    return HttpResponse(article_body)

@login_required(login_url='/admins/login/')
def addseries(request):
    if request.method == 'POST':
        blogmodels.Series.objects.create(name=request.POST.get('series'))
        return HttpResponseRedirect("/admins/addarticle")

@login_required(login_url='/admins/login/')
def adminweixin(request):
    if request.method == 'GET':
        Keywords3 =[]
        Keywords = blogmodels.KeyWord.objects.all()
        for item in Keywords:
            Keywords2 = {}
            Keywords2['id'] = item.id
            Keywords2['keyword'] = item.keyword
            Keywords2['content'] = json.loads(item.content)
            Keywords2['time'] = item.pub_date
            Keywords3.append(Keywords2)
        return render(request, 'admins/wechat.html', {'Keywords': Keywords3})
    if request.method == 'POST':
        blogmodels.KeyWord.objects.create(keyword=request.POST.get('keyword'), content=json.dumps(request.POST.get('content')))
    return HttpResponseRedirect("/admins/adminweixin/")

@login_required(login_url='/admins/login/')
def delwkey(request):
    if request.method == 'POST':
        blogmodels.KeyWord.objects.get(id=request.POST.get('modify')).delete()
        return HttpResponse(json.dumps('true'))

@login_required(login_url='/admins/login/')
def wxreply(request):
    if request.method == 'GET':
        Keywords3 = []
        Keywords = blogmodels.wxreply.objects.all()
        for item in Keywords:
            Keywords2 = {}
            Keywords2['id'] = item.id
            Keywords2['content'] = json.loads(item.content)
            Keywords2['time'] = item.pub_date
            Keywords3.append(Keywords2)
        return render(request, 'admins/wxreply.html', {'Keywords': Keywords3})
    if request.method == 'POST':
        blogmodels.wxreply.objects.create(content=json.dumps(request.POST.get('content')))
    return HttpResponseRedirect("/admins/wxreply/")

@login_required(login_url='/admins/login/')
def delreply(request):
    if request.method == 'POST':
        blogmodels.wxreply.objects.get(id=request.POST.get('modify')).delete()
        return HttpResponse(json.dumps('true'))

@login_required(login_url='/admins/login/')
def wxinstruction(request):
    if request.method == 'GET':
        Keywords3 = []
        Keywords = blogmodels.wxsetting.objects.all()
        for item in Keywords:
            Keywords2 = {}
            Keywords2['id'] = item.id
            Keywords2['keyword'] = item.keyword
            Keywords2['content'] = json.loads(item.content)
            Keywords2['time'] = item.pub_date
            Keywords3.append(Keywords2)
        return render(request, 'admins/instruction.html', {'Keywords': Keywords3})
    if request.method == 'POST':
        blogmodels.wxsetting.objects.create(keyword=request.POST.get('keyword'),
                                          content=json.dumps(request.POST.get('content')))
    return HttpResponseRedirect("/admins/wxinstruction/")


@login_required(login_url='/admins/login/')
def delinstruction(request):
    if request.method == 'POST':
        blogmodels.wxsetting.objects.get(id=request.POST.get('modify')).delete()
        return HttpResponse(json.dumps('true'))