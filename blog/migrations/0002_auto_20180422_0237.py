# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autho',
            new_name='author',
        ),
    ]