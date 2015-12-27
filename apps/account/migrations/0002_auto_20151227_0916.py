# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='abs_min_price',
            field=models.PositiveIntegerField(default=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='max_price',
            field=models.PositiveIntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='api_key',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='steam_username',
            field=models.CharField(default='username', max_length=255),
            preserve_default=False,
        ),
    ]
