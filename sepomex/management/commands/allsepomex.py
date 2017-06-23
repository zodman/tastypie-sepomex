#!/usr/bin/env python
# encoding=utf8
# made by zodman

from unicodecsv.py2 import UnicodeReader 
import glob
import logging
from tqdm import tqdm
import codecs
from django.core.management import call_command
from django.core.management.base import BaseCommand

from sepomex.models import MXEstado, MXAsentamiento, MXMunicipio
from sepomex.settings import FIELDNAMES

log = logging.getLogger('sepomex')

# COLUMNA DESCRIPCIÓN
# d_codigo Código Postal asentamiento
# d_asenta Nombre asentamiento
# d_tipo_asenta Tipo de asentamiento (Catálogo SEPOMEX)
# D_mnpio Nombre Municipio (INEGI, Marzo 2013)
# d_estado Nombre Entidad (INEGI, Marzo 2013)
# d_ciudad Nombre Ciudad (Catálogo SEPOMEX)
# d_CP Código Postal de la Administración Postal que reparte al asentamiento
# c_estado Clave Entidad (INEGI, Marzo 2013)
# c_oficina Código Postal de la Administración Postal que reparte al asentamiento
# c_CP Campo Vacio
# c_tipo_asenta Clave Tipo de asentamiento (Catálogo SEPOMEX)
# c_mnpio Clave Municipio (INEGI, Marzo 2013)
# id_asenta_cpcons Identificador único del asentamiento (nivel municipal)
# d_zona Zona en la que se ubica el asentamiento (Urbano/Rural)
# c_cve_ciudad Clave Ciudad (Catálogo SEPOMEX)

D_CODIGO = 0
D_ASENTA=1
D_TIPO_ASENTA=2
D_MNPIO = 3
D_ESTADO=4
D_CIUDAD=5
D_CP=6
C_ESTADO=7
C_OFICINA=8
C_CP=9
c_TIPO_ASENTA=10
C_MNPIO = 11
ID_ASENTA_CPCONS=12
D_ZONA=13
C_CVE_CIUDAD=14
STATES = u"""1|Aguascalientes|MX-AGU
2|Baja California|MX-BCN
3|Baja California Sur|MX-BCS
4|Campeche|MX-CAM
5|Coahuila de Zaragoza|MX-COA
6|Colima|MX-COL
7|Chiapas|MX-CHP
8|Chihuahua|MX-CHH
9|Distrito Federal|MX-DIF
10|Durango|MX-DUR
11|Guanajuato|MX-GUA
12|Guerrero|MX-GRO
13|Hidalgo|MX-HID
14|Jalisco|MX-JAL
15|México|MX-MEX
16|Michoacán de Ocampo|MX-MIC
17|Morelos|MX-MOR
18|Nayarit|MX-NAY
19|Nuevo León|MX-NLE
20|Oaxaca|MX-OAX
21|Puebla|MX-PUE
22|Querétaro|MX-QUE
23|Quintana Roo|MX-ROO
24|San Luis Potosí|MX-SLP
25|Sinaloa|MX-SIN
26|Sonora|MX-SON
27|Tabasco|MX-TAB
28|Tamaulipas|MX-TAM
29|Tlaxcala|MX-TLA
30|Veracruz de Ignacio de la Llave|MX-VER
31|Yucatán|MX-YUC
32|Zacatecas|MX-ZAC"""


def get_state(name_):
    lines = STATES.split("\n")
    for i in lines:
        id, name, abbr= i.split("|")
        if name == name_:
            return abbr


class Command(BaseCommand):
    help = 'Load sepomex database CPDescarga.txt into sepomex models'
    
    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):
        file = options["file"]
        with open(file, "r") as f:
            csvreader = UnicodeReader(f, delimiter="|")
            states =  self.create_states(csvreader)
            print "states %s" % len(states)

    def create_states(self, csvreader):
        states = set()
        index = 0
        for row in tqdm(csvreader):
            name = row[D_ESTADO]
            abbr = get_state(name)
            if abbr:
                s = (name, abbr)
                states.add(s)
        l = []
        for a, abb in states:
            l.append(MXEstado(nombre=a, abbr=abb))
        return MXEstado.objects.bulk_create(l)

