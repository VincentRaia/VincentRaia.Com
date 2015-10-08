# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20151007_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land',
            old_name='landing_title',
            new_name='object_title',
        ),
    ]
