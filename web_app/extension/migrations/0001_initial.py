# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100)),
                ('access_time', models.DateTimeField()),
                ('response', models.CharField(max_length=1, choices=[(b'L', b'like'), (b'D', b'dislike')])),
            ],
        ),
    ]
