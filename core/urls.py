# -*- coding: utf-8 -*-
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from core.api.viewsets import ParsedDataAPI


router = routers.DefaultRouter()
schema_view = get_schema_view(title='Pastebin API')

router.register('parsed_data', ParsedDataAPI, base_name='parsed_data')

urlpatterns = [
    # api
    path('', include(router.urls)),
    path('schema/', login_required(schema_view)),
]
