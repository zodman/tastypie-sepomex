# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sepomex', '0002_auto_20151113_1937'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mxmunicipio',
            unique_together=set([('clave', 'nombre', 'mx_estado')]),
        ),
    ]
