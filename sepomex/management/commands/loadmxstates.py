# -*- coding: utf-8 -*-

import csv

from django.core.management.base import BaseCommand, CommandError
from sepomex.models import MXEstado


class Command(BaseCommand):
    help = 'Load states objects from csv file'

    def handle(self, *args, **options):
        with open('data/sepomex_mx_states.txt') as mxstates_file:
            reader = csv.reader(mxstates_file, delimiter='|')
            mxstates = [
                MXEstado(id=index+1, abbr=state[1], nombre=state[0])
                for index, state in enumerate(reader)
            ]
            MXEstado.objects.bulk_create(mxstates)
        print 'mxstates created!'
