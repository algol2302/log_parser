from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters import rest_framework as django_filters
# from django.contrib.auth.models import User
# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator
# from django.conf import settings
# from django.core.cache import caches

from core.models import ParsedData
from core.api.serializers import ParsedDataSerializer
from core.api.filters import ParsedDataFilter


class ParsedDataAPI(ModelViewSet):
    serializer_class = ParsedDataSerializer
    queryset = ParsedData.objects.all()

    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

    filter_backends = (
        filters.SearchFilter,
        django_filters.DjangoFilterBackend,
    )

    filter_class = ParsedDataFilter
    search_fields = (
        'ip_addr', 'http_method', 'log_date',
        'uri', 'error_code',
    )
