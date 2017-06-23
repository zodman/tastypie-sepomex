# -*- coding: utf-8 -*-

from unicodecsv.py2 import DictReader
import glob
import logging

from tqdm import tqdm
from django.core.management.base import BaseCommand

from sepomex.models import MXEstado, MXMunicipio
from sepomex.settings import FIELDNAMES

log = logging.getLogger('sepomex')


files = glob.glob('data/municipalities/*txt')

class Command(BaseCommand):
    def handle(self, *args, **options):
        municipalities = []
        for name in tqdm(files):
            with open(name) as municipalities_file:
                reader = DictReader(municipalities_file,
                                        delimiter='|',
                                        fieldnames=FIELDNAMES)
                municipality = reader.next()
                state = MXEstado.objects.get(id=municipality['c_estado'])

                municipalities.append(
                    MXMunicipio(nombre=municipality['D_mnpio'],
                        clave=municipality['c_mnpio'],
                        mx_estado=state
                    )
                )

        MXMunicipio.objects.bulk_create(municipalities)

        log.info(u'{} municipios creados!'.format(len(municipalities)))
