# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-25 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20170124_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='\u5168\u56fd\u77e5\u540d', max_length=10, verbose_name='\u673a\u6784\u6807\u7b7e'),
        ),
    ]
