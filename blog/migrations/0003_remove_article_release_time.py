# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170418_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='release_time',
        ),
    ]
