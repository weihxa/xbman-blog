# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(max_length=255, unique=True, serialize=False, verbose_name='\u90ae\u7bb1', primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('token', models.CharField(default=None, max_length=128, null=True, verbose_name='token', blank=True)),
                ('department', models.CharField(default=None, max_length=32, null=True, verbose_name='\u90e8\u95e8', blank=True)),
                ('tel', models.CharField(default=None, max_length=32, null=True, verbose_name='\u5ea7\u673a', blank=True)),
                ('mobile', models.CharField(default=None, max_length=32, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('memo', models.TextField(default=None, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('valid_begin_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_end_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, verbose_name='\u6807\u9898')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('body', models.TextField(verbose_name='\u6b63\u6587')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('status', models.CharField(default=0, max_length=1, verbose_name='\u72b6\u6001', choices=[(b'0', b'\xe5\x8f\x91\xe5\xb8\x83'), (b'1', b'\xe5\xad\x98\xe7\xa8\xbf')])),
                ('read', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u6570')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u8868',
                'verbose_name_plural': '\u6587\u7ae0\u8868',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x8f\x91\xe5\x87\xba\xe7\x9a\x84\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d', max_length=256, verbose_name=b'\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d')),
                ('content', models.TextField(help_text=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe7\xbb\x99\xe7\x94\xa8\xe6\x88\xb7\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9', null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u5173\u952e\u8bcd',
                'verbose_name_plural': '\u5fae\u4fe1\u5173\u952e\u8bcd',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('url', models.URLField(unique=True)),
                ('description', models.CharField(default=b'\xe6\xad\xa4\xe7\x94\xa8\xe6\x88\xb7\xe6\xb2\xa1\xe6\x9c\x89\xe6\xb7\xbb\xe5\x8a\xa0\xe4\xbb\xbb\xe4\xbd\x95\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField(verbose_name='\u535a\u4e3b\u4fe1\u606f')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='wxreply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(help_text=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe5\x86\x85\xe5\xae\xb9', null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
            ],
            options={
                'verbose_name': '\u968f\u673a\u56de\u590d',
                'verbose_name_plural': '\u968f\u673a\u56de\u590d',
            },
        ),
        migrations.CreateModel(
            name='wxsetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x8f\x91\xe5\x87\xba\xe7\x9a\x84\xe6\x8c\x87\xe4\xbb\xa4', max_length=256, verbose_name=b'\xe6\x8c\x87\xe4\xbb\xa4')),
                ('content', models.TextField(help_text=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe7\xbb\x99\xe7\x94\xa8\xe6\x88\xb7\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9', null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u6307\u4ee4',
                'verbose_name_plural': '\u5fae\u4fe1\u6307\u4ee4',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='blog.Categories', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='article',
            name='series',
            field=models.ForeignKey(verbose_name='\u7cfb\u5217', to='blog.Series', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]
