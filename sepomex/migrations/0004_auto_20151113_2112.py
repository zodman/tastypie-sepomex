# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sepomex', '0003_auto_20151113_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mxestado',
            name='abbr',
            field=models.CharField(max_length=6, unique=True, null=True),
        ),
    ]
