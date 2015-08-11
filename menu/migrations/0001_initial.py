# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=48)),
                ('tag', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ordering', models.IntegerField(auto_created=True)),
                ('label', models.CharField(max_length=64)),
                ('link', models.CharField(default='', blank=True, max_length=128)),
                ('enabled', models.BooleanField(default=True)),
                ('type', models.CharField(default='hash', max_length=64, choices=[('hash', 'Hash'), ('slash', 'Regular'), ('link', 'External'), ('user', 'User')])),
                ('menu', models.ForeignKey(to='menu.Menu')),
                ('parent', models.ForeignKey(blank=True, null=True, to='menu.MenuItem')),
            ],
        ),
    ]
