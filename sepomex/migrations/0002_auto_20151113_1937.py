# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sepomex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mxmunicipio',
            name='clave',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mxmunicipio',
            name='mx_estado',
            field=models.ForeignKey(related_name='municipios', to='sepomex.MXEstado'),
        ),
    ]
