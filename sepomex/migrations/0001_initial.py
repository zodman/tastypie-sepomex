# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MXAsentamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('tipo_asentamiento', models.CharField(max_length=100)),
                ('zona', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=5, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MXEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('abbr', models.CharField(max_length=5, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MXMunicipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('clave', models.CharField(unique=True, max_length=10)),
                ('mx_estado', models.ForeignKey(to='sepomex.MXEstado')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='mxestado',
            unique_together=set([('nombre', 'abbr')]),
        ),
        migrations.AddField(
            model_name='mxasentamiento',
            name='mx_municipio',
            field=models.ForeignKey(to='sepomex.MXMunicipio'),
        ),
        migrations.AlterUniqueTogether(
            name='mxmunicipio',
            unique_together=set([('clave', 'nombre')]),
        ),
        migrations.AlterUniqueTogether(
            name='mxasentamiento',
            unique_together=set([('mx_municipio', 'cp', 'nombre')]),
        ),
    ]
