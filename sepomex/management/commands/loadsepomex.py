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

            for name in tqdm(files):
                with open(name) as municipalities_file:
                    reader = DictReader(municipalities_file,
                                            delimiter='|',
                                            fieldnames=FIELDNAMES)

                    municipality = next(reader)
                    [municipality.update({k:v}) for k,v in municipality.items()]
                    state = MXEstado.objects.get(id=municipality['c_estado'])
                    municipio = MXMunicipio.objects.get(
                        clave=municipality['c_mnpio'], mx_estado=state,
                        nombre=municipality['D_mnpio'])
                    ciudad, _ = MXCiudad.objects.get_or_create(
                                        nombre=municipality["d_ciudad"], mx_estado=state)
                    asentamientos = []
                    for item in tqdm(reader):
                        [item.update({k:v}) for k,v in item.items()]
                        asentamientos.append(MXAsentamiento(
                            cp=item['d_codigo'], nombre=item['d_asenta'],
                            tipo_asentamiento=item['d_tipo_asenta'],
                            zona=item['d_zona'], mx_municipio=municipio,
                            mx_ciudad=ciudad,
                        ))
                    MXAsentamiento.objects.bulk_create(asentamientos)
            log.info("{} Asentamientos creados".format(MXAsentamiento.objects.all().count()))
