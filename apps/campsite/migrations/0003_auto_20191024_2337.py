# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-24 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campsite', '0002_campground_reservation_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campground',
            old_name='contractCode',
            new_name='park_id',
        ),
    ]
