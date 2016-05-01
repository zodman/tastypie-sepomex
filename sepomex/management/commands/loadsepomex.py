# -*- coding: utf-8 -*-

import csv
import glob

from django.core.management import call_command
from django.core.management.base import BaseCommand

from sepomex.models import MXEstado, MXAsentamiento, MXMunicipio
from sepomex.settings import FIELDNAMES


class Command(BaseCommand):
    help = 'Load sepomex database into sepomex models'

    def handle(self, *args, **options):
        if MXEstado.objects.count() == 0:
            call_command('loadmxstates')

        if MXMunicipio.objects.count() == 0:
            call_command('loadmxmunicipalities')

        if MXAsentamiento.objects.count() == 0:
            files = glob.glob('data/municipalities/*txt')

            for name in files:
                with open(name) as municipalities_file:
                    reader = csv.DictReader(municipalities_file,
                                            delimiter='|',
                                            fieldnames=FIELDNAMES)

                    municipality = reader.next()

                    state = MXEstado.objects.get(id=municipality['c_estado'])
                    municipio = MXMunicipio.objects.get(
                        clave=municipality['c_mnpio'], mx_estado=state,
                        nombre=municipality['D_mnpio'].decode('latin-1'))

                    asentamientos = [
                        MXAsentamiento(
                            cp=municipality['d_codigo'],
                            nombre=municipality['d_asenta'],
                            tipo_asentamiento=municipality['d_tipo_asenta'],
                            zona=municipality['d_zona'], mx_municipio=municipio,
                        )
                    ]

                    asentamientos += [
                        MXAsentamiento(
                            cp=item['d_codigo'], nombre=item['d_asenta'],
                            tipo_asentamiento=item['d_tipo_asenta'],
                            zona=item['d_zona'], mx_municipio=municipio
                        ) for item in reader
                    ]

                    MXAsentamiento.objects.bulk_create(asentamientos)

                    print u'{}: {} asentamientos creados'.format(
                        municipio.nombre, len(asentamientos))
