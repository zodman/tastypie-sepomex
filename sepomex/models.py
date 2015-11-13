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


class MXEstado(models.Model):
    nombre = models.CharField(max_length=200)
    abbr = models.CharField(max_length=6, null=True, unique=True)

    class Meta:
        unique_together = ('nombre', 'abbr')

    def __unicode__(self):
        return u'{0} - {1}'.format(self.abbr, self.nombre)


class MXMunicipio(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=10)

    mx_estado = models.ForeignKey(MXEstado, related_name='municipios')

    class Meta:
        unique_together = ('clave', 'nombre', 'mx_estado')

    def __unicode__(self):
        return self.nombre


class MXAsentamiento(models.Model):
    nombre = models.CharField(max_length=200)

    mx_municipio = models.ForeignKey(MXMunicipio, related_name='municipio')
    tipo_asentamiento = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    cp = models.CharField(max_length=5, null=True)


    def __unicode__(self):
        return self.nombre
