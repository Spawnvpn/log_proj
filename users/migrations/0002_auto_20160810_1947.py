# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webstoreuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='webstoreuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='WebStoreUser',
        ),
    ]