# -*- coding: utf-8 -*-

from django.http import HttpResponse
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, ForeignKey
from ..models import MXEstado, MXMunicipio, MXAsentamiento


def build_content_type(format, encoding='utf-8'):
    """
    Appends character encoding to the provided format if not already present.
    """
    if 'charset' in format:
        return format

    return "%s; charset=%s" % (format, encoding)


class BaseModelResource(ModelResource):
    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.

        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        return response_class(content=serialized, content_type=build_content_type(desired_format), **response_kwargs)


class AsentamientoResource(BaseModelResource):
    class Meta:
        queryset = MXAsentamiento.objects.all().order_by('nombre')


class EstadoResource(BaseModelResource):
    class Meta:
        queryset = MXEstado.objects.all().order_by('nombre')
        filtering = {
            'id': ALL,
            'nombre': 'exact',
        }


class MunicipioResource(BaseModelResource):
    class Meta:
        queryset = MXMunicipio.objects.all().order_by('nombre')
        filtering = {
            'clave': 'exact',
            'nombre': 'exact',
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
