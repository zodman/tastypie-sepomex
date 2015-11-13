# -*- coding: utf-8 -*-

"""
d_codigo Código Postal asentamiento
d_asenta Nombre asentamiento
d_tipo_asenta Tipo de asentamiento (Catálogo SEPOMEX)
d_CP Código Postal de la Administración Postal que reparte al asentamiento
c_oficina Código Postal de la Administración Postal que reparte al asentamiento
c_tipo_asenta Clave Tipo de asentamiento (Catálogo SEPOMEX)
id_asenta_cpcons Identificador único del asentamiento (nivel municipal)
d_zona Zona en la que se ubica el asentamiento (Urbano/Rural)

D_mnpio Nombre Municipio (INEGI, Marzo 2013)
c_mnpio Clave Municipio (INEGI, Marzo 2013)

d_estado Nombre Entidad (INEGI, Marzo 2013)
c_estado Clave Entidad (INEGI, Marzo 2013)

d_ciudad Nombre Ciudad (Catálogo SEPOMEX)
c_cve_ciudad Clave Ciudad (Catálogo SEPOMEX)

c_CP Campo Vacio
"""

from django.db import models
