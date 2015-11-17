# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, ForeignKey
from ..models import MXEstado, MXMunicipio, MXAsentamiento


class AsentamientoResource(ModelResource):
    class Meta:
        queryset = MXAsentamiento.objects.all()


class EstadoResource(ModelResource):
    class Meta:
        queryset = MXEstado.objects.all()
        filtering = {
            'id': ALL
        }


class MunicipioResource(ModelResource):
    class Meta:
        queryset = MXMunicipio.objects.all()
        filtering = {
            'clave': 'exact',
        }


class MXMunicipioResource(MunicipioResource):
    mx_estado = ForeignKey(EstadoResource, 'mx_estado', null=True, full=True)
    # asentamientos = ToManyField(AsentamientoResource, 'municipio', full=True)

    class Meta(MunicipioResource.Meta):
        allowed_methods = ['get']
        MunicipioResource.Meta.filtering['mx_estado'] = ALL_WITH_RELATIONS


class MXEstadoResource(EstadoResource):
    class Meta(EstadoResource.Meta):
        allowed_methods = ['get']


class MXAsentamientoResource(AsentamientoResource):
    municipio = ForeignKey(MunicipioResource, 'mx_municipio', null=True,
                           full=True)

    class Meta(AsentamientoResource.Meta):
        allowed_methods = ['get']
        filtering = {
            'cp': 'exact',
            'tipo_asentamiento': 'iexact',
            'municipio': ALL_WITH_RELATIONS
        }
