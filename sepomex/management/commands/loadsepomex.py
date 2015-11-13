# -*- coding: utf-8 -*-

import csv
import sys
import glob

from django.core.management import call_command
from django.core.management.base import BaseCommand
from sepomex.models import MXEstado, MXMunicipio


class Command(BaseCommand):
    help = 'Load sepomex database into sepomex models'

    def handle(self, *args, **options):
        MXEstado.objects.all().delete()
        MXMunicipio.objects.all().delete()
        call_command('loadmxstates')

        files = glob.glob('data/municipalities/*txt')

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

        print 'TOTAL COUNT', len(municipalities), MXMunicipio.objects.count(), len(files)

        MXMunicipio.objects.bulk_create(municipalities)
