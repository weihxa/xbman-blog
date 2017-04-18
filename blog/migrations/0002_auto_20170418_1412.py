# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('url', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('release_time', models.DateTimeField(default=b'1970-1-1 00:00:00')),
                ('status', models.CharField(default=0, max_length=1, choices=[(b'0', b'\xe5\x8f\x91\xe5\xb8\x83'), (b'1', b'\xe5\xad\x98\xe7\xa8\xbf')])),
                ('read', models.IntegerField(default=0)),
            ],
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
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('keywords', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to=b'%Y/%m')),
                ('homedescription', models.CharField(max_length=150)),
                ('recordinfo', models.CharField(max_length=100)),
                ('statisticalcode', models.TextField()),
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
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='blog.Categories'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
