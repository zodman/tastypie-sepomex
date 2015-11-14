# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from tastypie.fields import ToManyField, ForeignKey
from ..models import MXEstado, MXMunicipio, MXAsentamiento


class AsentamientoResource(ModelResource):
    class Meta:
        queryset = MXAsentamiento.objects.all()


class EstadoResource(ModelResource):
    class Meta:
        queryset = MXEstado.objects.all()


class MunicipioResource(ModelResource):
    class Meta:
        queryset = MXMunicipio.objects.all()


class MXMunicipioResource(MunicipioResource):
    Estado = ForeignKey(EstadoResource, 'mx_estado', null=True, full=True)
    # asentamientos = ToManyField(AsentamientoResource, 'municipio', full=True)

    class Meta(MunicipioResource.Meta):
        allowed_methods = ['get']
        filtering = {
            'nombre': 'exact',
        }


class MXEstadoResource(EstadoResource):
    class Meta(EstadoResource.Meta):
        allowed_methods = ['get']


class MXAsentamientoResource(AsentamientoResource):
    municipio = ForeignKey(MunicipioResource, 'mx_municipio', null=True,
                           full=True)

    class Meta(AsentamientoResource.Meta):
        allowed_methods = ['get']
        filtering = {
            'cp': 'exact'
        }
