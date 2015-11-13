# -*- coding: utf-8 -*-

import csv
import glob

from django.core.management import call_command
from django.core.management.base import BaseCommand

from sepomex.models import MXEstado, MXAsentamiento, MXMunicipio


class Command(BaseCommand):
    help = 'Load sepomex database into sepomex models'

    def handle(self, *args, **options):
        MXEstado.objects.all().delete()
        call_command('loadmxstates')

        MXMunicipio.objects.all().delete()
        call_command('loadmxmunicipalities')

        MXAsentamiento.objects.all().delete()
        files = glob.glob('data/municipalities/*txt')

        for name in files:
            with open(name) as municipalities_file:
                reader = csv.reader(municipalities_file, delimiter='|')

                municipality = reader.next()
                municipio = MXMunicipio.objects.filter(
                    clave=municipality[11],
                    nombre=municipality[3].decode('latin-1'))

                asentamientos = [
                    MXAsentamiento(
                        cp=item[0], nombre=item[1], tipo_asentamiento=item[2],
                        zona=item[13], mx_municipio=municipio[0]
                    ) for item in reader
                ]

                MXAsentamiento.objects.bulk_create(asentamientos)

                print u'{}: {} asentamientos creados'.format(
                    municipio.nombre, len(asentamientos)))
