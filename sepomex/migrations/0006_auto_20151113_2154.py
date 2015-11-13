# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sepomex', '0005_auto_20151113_2149'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mxasentamiento',
            unique_together=set([]),
        ),
    ]
