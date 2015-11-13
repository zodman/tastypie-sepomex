# -*- coding: utf-8 -*-

import csv
import glob

from django.core.management.base import BaseCommand
from sepomex.models import MXEstado, MXMunicipio


files = glob.glob('data/municipalities/*txt')

class Command(BaseCommand):
    def handle(self, *args, **options):
        municipalities = []
        for name in files:
            with open(name) as municipalities_file:
                reader = csv.reader(municipalities_file, delimiter='|')

                municipality = reader.next()
                state = MXEstado.objects.get(id=municipality[7])

                municipalities.append(
                    MXMunicipio(nombre=municipality[3].decode('latin-1'),
                                clave=municipality[11], mx_estado=state)
                )

        MXMunicipio.objects.bulk_create(municipalities)

        print u'{} municipios creados!'.format(len(municipalities))
