#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'weihaoxuan'
from django.shortcuts import render
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib import auth
import django



def login(request):
    if request.method == "POST":

        username = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.valid_end_time: #设置了end time
                if django.utils.timezone.now() > user.valid_begin_time and django.utils.timezone.now()  < user.valid_end_time:
                    auth.login(request,user)
                    request.session.set_expiry(60*30)
                    return HttpResponseRedirect('/admins/index/')
                else:
                    return render(request,'admins/login.html',{'login_err': 'User account is expired,please contact your IT guy for this!'})
            elif django.utils.timezone.now() > user.valid_begin_time:
                    auth.login(request,user)
                    request.session.set_expiry(60*30)
                    return HttpResponseRedirect('/admins/index/')

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
    return render(request, 'admins/index.html',
                  context_instance=RequestContext(request))