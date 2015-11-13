# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sepomex', '0004_auto_20151113_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mxasentamiento',
            name='cp',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='mxasentamiento',
            name='mx_municipio',
            field=models.ForeignKey(related_name='municipio', to='sepomex.MXMunicipio'),
        ),
    ]
