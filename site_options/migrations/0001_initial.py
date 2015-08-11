# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('key', models.CharField(max_length=128, verbose_name='Option', choices=[('shop_name', 'Shop name'), ('footer_text', 'Footer text')])),
                ('value', models.CharField(max_length=128, verbose_name='Value')),
            ],
        ),
    ]
