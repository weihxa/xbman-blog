# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2017, 10, 19, 11, 43, 55, 142000), verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
