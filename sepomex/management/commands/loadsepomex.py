from unicodecsv.py2 import DictReader
import glob
import logging
from tqdm import tqdm
from django.core.management import call_command
from django.core.management.base import BaseCommand

from sepomex.models import MXEstado, MXAsentamiento, MXMunicipio, MXCiudad
from sepomex.settings import FIELDNAMES

log = logging.getLogger('sepomex')

class Command(BaseCommand):
    help = 'Load sepomex database into sepomex models'

    def handle(self, *args, **options):
        if MXEstado.objects.count() == 0:
            call_command('loadmxstates')

        if MXMunicipio.objects.count() == 0:
            call_command('loadmxmunicipalities')

        if MXAsentamiento.objects.count() == 0:
            files = glob.glob('data/municipalities/*txt')
            print("#### {} #### {}".format(len(files),2457))
            for name in tqdm(files):
                if "MX-14" in name and '030' in name:
                    print name
                with open(name) as municipalities_file:
                    reader = DictReader(municipalities_file,
                                            delimiter='|',
                                            fieldnames=FIELDNAMES)
                    l = []
                    for municipality in tqdm(reader):
                        item = municipality.copy()
                        if "MX-14" in name and  '030' in name:
                            print(">{}".format(municipality))
                        [municipality.update({k:v}) for k,v in municipality.items()]
                        state = MXEstado.objects.get(id=municipality['c_estado'])
                        municipio = MXMunicipio.objects.get(
                            clave=municipality['c_mnpio'], mx_estado=state,
                            nombre=municipality['D_mnpio'])
                        ciudad, _ = MXCiudad.objects.get_or_create(
                                            nombre=municipality["d_ciudad"], mx_estado=state)
                        [item.update({k:v}) for k,v in item.items()]
                        a =MXAsentamiento(
                            cp=item['d_codigo'], nombre=item['d_asenta'],
                            tipo_asentamiento=item['d_tipo_asenta'],
                            zona=item['d_zona'], mx_municipio=municipio,
                            mx_ciudad=ciudad,
                        )
                        if item['d_codigo'] == '45901':
                            print(item)
                            print("=========")
                        l.append(a)
                        if item['d_codigo'] == '45901':
                            print("=========")
                            print("CP id {}".format(a.id))
                            assert False, o
                MXAsentamiento.objects.bulk_create(l)
            log.info("{} Asentamientos creados".format(MXAsentamiento.objects.all().count()))
