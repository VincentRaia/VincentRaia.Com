# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('landing_title', models.CharField(max_length=255)),
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
        migrations.DeleteModel(
            name='Land',
        ),
    ]
