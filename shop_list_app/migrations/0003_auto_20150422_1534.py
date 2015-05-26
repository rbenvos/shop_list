# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop_list_app', '0002_auto_20150421_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_tlf_and',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
