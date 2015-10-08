# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=255)),
                ('tagline', models.CharField(max_length=255)),
                ('aboutme_heading', models.CharField(max_length=255)),
                ('aboutme_text', models.TextField()),
                ('aboutblog_heading', models.CharField(max_length=255)),
                ('aboutblog_text', models.TextField()),
                ('contact_heading', models.CharField(max_length=255)),
                ('contact_text', models.TextField()),
            ],
        ),
    ]
