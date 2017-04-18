#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'weihaoxuan'
from django.contrib import admin
from blog import models
from user_admin import UserAdmin
from django.contrib.auth.models import Group
# Register your models here.
class device_config(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
admin.site.register(models.UserProfile,UserAdmin)
admin.site.register(models.Article,)
admin.site.register(models.Categories,)
admin.site.register(models.Tag,)
admin.site.register(models.Link,)
admin.site.register(models.Setting,)
admin.site.unregister(Group)