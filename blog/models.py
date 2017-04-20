#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'weihaoxuan'
from django.db import models
from blog.user_models import UserProfile

class Categories(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def categories_article_count(self):
        return self.article_set.all().count()


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def tag_article_count(self):
        return self.article_set.all().count()

class Series(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    STATUS_CHOICES = (
        ('0', '发布'),
        ('1', '存稿'),
    )

    title = models.CharField(u'标题',max_length=255, unique=True)
    description = models.TextField(u'描述',)
    body = models.TextField(u'正文',)
    created_time = models.DateTimeField(u'创建时间',auto_now_add=True)
    # release_time = models.DateTimeField(default='1970-1-1 00:00:00')
    status = models.CharField(u'状态',default=0, max_length=1, choices=STATUS_CHOICES)
    read = models.IntegerField(u'阅读数',default=0)
    categories = models.ManyToManyField(Categories,verbose_name=u'分类')
    tag = models.ManyToManyField(Tag,verbose_name=u'标签')
    series = models.ForeignKey(Series,verbose_name=u'系列',null=True)

    def get_tag(self):
        tag = ''
        for t in self.tag.all():
            tag += ',' + t.name
        return tag.strip(',')

    def get_categories(self):
        categories = ''
        for c in self.categories.all():
            categories += ',' + c.name
        return categories.strip(',')

    def get_tags(self):
        return Tag.objects.filter(article=self.pk)

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = "文章表"



class Link(models.Model):
    name = models.CharField(max_length=32, unique=True)
    url = models.URLField(unique=True)
    description = models.CharField(max_length=255, default='此用户没有添加任何描述')
    add_time = models.DateTimeField(auto_now_add=True)


class Setting(models.Model):
    body = models.TextField(u'博主信息', )
