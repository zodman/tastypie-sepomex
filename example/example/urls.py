from django.conf.urls import include, url

from tastypie.api import Api
from sepomex.api import MXEstadoResource, MXMunicipioResource


api_v1 = Api(api_name='v1')
api_v1.register(MXEstadoResource())
api_v1.register(MXMunicipioResource())


urlpatterns = [
    url('^api/', include(api_v1.urls)),
]
