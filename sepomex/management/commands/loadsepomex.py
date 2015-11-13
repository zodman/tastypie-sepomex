# -*- coding: utf-8 -*-

from __future__ import print_function

import csv

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Load sepomex database into sepomex models'

    def handle(self, *args, **options):
        call_command('loadmxstates')
