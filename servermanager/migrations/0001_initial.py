# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-17 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name=b'\xe5\x91\xbd\xe4\xbb\xa4\xe6\xa0\x87\xe9\xa2\x98')),
                ('command', models.CharField(max_length=2000, verbose_name=b'\xe5\x91\xbd\xe4\xbb\xa4')),
                ('describe', models.CharField(max_length=300, verbose_name=b'\xe5\x91\xbd\xe4\xbb\xa4\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u547d\u4ee4',
                'verbose_name_plural': '\u547d\u4ee4',
            },
        ),
        migrations.CreateModel(
            name='EmailSendLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailto', models.CharField(max_length=300, verbose_name=b'\xe6\x94\xb6\xe4\xbb\xb6\xe4\xba\xba')),
                ('title', models.CharField(max_length=2000, verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe5\x86\x85\xe5\xae\xb9')),
                ('send_result', models.BooleanField(default=False, verbose_name=b'\xe7\xbb\x93\xe6\x9e\x9c')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-created_time'],
                'verbose_name': '\u90ae\u4ef6\u53d1\u9001log',
                'verbose_name_plural': '\u90ae\u4ef6\u53d1\u9001log',
            },
        ),
    ]
