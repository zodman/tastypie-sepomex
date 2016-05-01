# -*- coding: utf-8 -*-

import csv
import glob

from django.core.management.base import BaseCommand

from sepomex.models import MXEstado, MXMunicipio
from sepomex.settings import FIELDNAMES


files = glob.glob('data/municipalities/*txt')

class Command(BaseCommand):
    def handle(self, *args, **options):
        municipalities = []
        for name in files:
            with open(name) as municipalities_file:
                reader = csv.DictReader(municipalities_file,
                                        delimiter='|',
                                        fieldnames=FIELDNAMES)
                municipality = reader.next()
                state = MXEstado.objects.get(id=municipality['c_estado'])

                municipalities.append(
                    MXMunicipio(nombre=municipality['D_mnpio'].decode('latin-1'),
                        clave=municipality['c_mnpio'],
                        mx_estado=state
                    )
                )

        MXMunicipio.objects.bulk_create(municipalities)

        print u'{} municipios creados!'.format(len(municipalities))
