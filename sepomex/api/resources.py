# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from tastypie.fields import ToManyField, ForeignKey
from ..models import MXEstado, MXMunicipio, MXAsentamiento


class MXMunicipioResource(ModelResource):
    Estado = ForeignKey('sepomex.api.MXEstadoResource', 'mx_estado', null=True)

    class Meta:
        queryset = MXMunicipio.objects.all()
        allowed_methods = ['get']
        filtering = {
            'nombre': 'exact'
        }


class MXEstadoResource(ModelResource):
    municipios = ToManyField(MXMunicipioResource, 'municipios', null=True,
                             full=True)

    class Meta:
        queryset = MXEstado.objects.all()
        allowed_methods = ['get']


class MXAsentamientoResource(ModelResource):
    municipio = ForeignKey(MXMunicipioResource, 'mx_municipio', null=True,
                           full=True)

    class Meta:
        queryset = MXAsentamiento.objects.all()
        allowed_methods = ['get']
        filtering = {
            'cp': 'exact'
        }
