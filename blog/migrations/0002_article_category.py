# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default=0, max_length=1, verbose_name='\u7c7b\u522b', choices=[(b'0', b'\xe5\x8e\x9f\xe5\x88\x9b'), (b'1', b'\xe8\xbd\xac\xe8\xbd\xbd')]),
        ),
    ]
