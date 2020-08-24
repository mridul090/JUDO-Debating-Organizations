# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-08-20 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_req',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('Email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('Message', models.TextField(verbose_name='Message')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
