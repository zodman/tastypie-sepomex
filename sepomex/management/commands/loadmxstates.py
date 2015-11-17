# -*- coding: utf-8 -*-

import csv

from django.core.management.base import BaseCommand, CommandError
from sepomex.models import MXEstado


class Command(BaseCommand):
    help = 'Load states objects from csv file'

    def handle(self, *args, **options):
        MXEstado.objects.all().delete()
        with open('data/sepomex_mx_states.txt') as mxstates_file:
            reader = csv.reader(mxstates_file, delimiter='|')
            mxstates = [
                MXEstado(id=state[0], abbr=state[2], nombre=state[1])
                for state in reader
            ]
            MXEstado.objects.bulk_create(mxstates)
        print u'{} Estados creados!'.format(len(mxstates))
