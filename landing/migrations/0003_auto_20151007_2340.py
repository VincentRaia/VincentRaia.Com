# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20151007_2339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Landing',
            new_name='Land',
        ),
    ]
