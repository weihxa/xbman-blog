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
    ]
