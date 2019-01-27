from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache import caches

from core.models import ParsedData
from core.api.serializers import ParsedDataSerializer


class ParsedDataAPI(ModelViewSet):
    serializer_class = ParsedDataSerializer
