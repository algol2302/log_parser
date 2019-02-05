# -*- coding: utf-8 -*-
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from rest_framework import routers
# from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.api.viewsets import ParsedDataAPI


router = routers.DefaultRouter()
# schema_view = get_schema_view(title='Pastebin API')
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router.register('parsed_data', ParsedDataAPI, base_name='parsed_data')

urlpatterns = [
    # api
    path('', include(router.urls)),
    # path('schema/', login_required(schema_view)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
