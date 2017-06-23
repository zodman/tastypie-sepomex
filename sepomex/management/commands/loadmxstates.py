# -*- coding: utf-8 -*-
from unicodecsv.py2 import DictReader
import csv
import logging
from django.core.management.base import BaseCommand, CommandError
from sepomex.models import MXEstado

log = logging.getLogger('sepomex')

class Command(BaseCommand):
    help = 'Load states objects from csv file'

    def handle(self, *args, **options):
        MXEstado.objects.all().delete()
        with open('data/sepomex_mx_states.txt') as mxstates_file:
            reader = DictReader(mxstates_file,
                                    delimiter='|',
                                    fieldnames=['id', 'name', 'abbr'])
            mxstates = [
                MXEstado(id=state['id'], abbr=state['abbr'], nombre=state['name'])
                for state in reader
            ]
            MXEstado.objects.bulk_create(mxstates)
        log.info(u'{} Estados creados!'.format(len(mxstates)))
