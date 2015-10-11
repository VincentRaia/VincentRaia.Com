# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20151007_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='aboutblog_text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='land',
            name='aboutme_text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='land',
            name='contact_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
