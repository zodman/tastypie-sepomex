# -*- coding: utf-8 -*-

import csv
import glob
import logging

from django.core.management.base import BaseCommand

from sepomex.models import MXEstado, MXMunicipio
from sepomex.settings import FIELDNAMES

log = logging.getLogger('sepomex')


files = glob.glob('data/municipalities/*txt')

class Command(BaseCommand):
    def handle(self, *args, **options):
        municipalities = []
        for name in files:
            with open(name, encoding='latin-1') as municipalities_file:
                reader = csv.DictReader(municipalities_file,
                                        delimiter='|',
                                        fieldnames=FIELDNAMES)
                municipality = next(reader)
                state = MXEstado.objects.get(id=municipality['c_estado'])

                municipalities.append(
                    MXMunicipio(nombre=municipality['D_mnpio'],
                        clave=municipality['c_mnpio'],
                        mx_estado=state
                    )
                )

        MXMunicipio.objects.bulk_create(municipalities)

        log.info(u'{} municipios creados!'.format(len(municipalities)))
