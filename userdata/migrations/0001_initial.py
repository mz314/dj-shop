# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('city', models.CharField(max_length=128)),
                ('zip', models.CharField(max_length=16)),
                ('street', models.CharField(max_length=128)),
                ('street_number', models.CharField(max_length=128)),
                ('country', models.ForeignKey(to='userdata.Country')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
