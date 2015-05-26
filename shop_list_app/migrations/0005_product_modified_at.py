# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop_list_app', '0004_auto_20150422_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True),
        ),
    ]
