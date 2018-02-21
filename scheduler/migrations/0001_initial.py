# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(max_length=250)),
                ('content', models.CharField(max_length=1000)),
                ('image_url', models.CharField(max_length=250)),
                ('to_be_sended_on', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
