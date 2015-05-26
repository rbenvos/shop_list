# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop_list_app', '0003_auto_20150422_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True),
        ),
    ]
