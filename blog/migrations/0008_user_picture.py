# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170527_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to='picture'),
        ),
    ]
