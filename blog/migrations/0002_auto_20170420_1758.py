# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='series',
            field=models.ForeignKey(verbose_name='\u7cfb\u5217', to='blog.Series', null=True),
        ),
    ]
