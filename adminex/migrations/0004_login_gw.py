# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-06 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminex', '0003_delete_login_gw'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_gw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pwd', models.TextField()),
            ],
        ),
    ]
