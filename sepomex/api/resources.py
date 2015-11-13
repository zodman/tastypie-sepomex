# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource
from tastypie.fields import ToManyField
from ..models import MXEstado, MXMunicipio


class MXMunicipioResource(ModelResource):
    class Meta:
        queryset = MXMunicipio.objects.all()
        allowed_methods = ['get']


class MXEstadoResource(ModelResource):
    municipios = ToManyField(MXMunicipioResource, 'municipios', null=True,
                             full=True)

    class Meta:
        queryset = MXEstado.objects.all()
        allowed_methods = ['get']
