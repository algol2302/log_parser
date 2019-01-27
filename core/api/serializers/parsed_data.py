from rest_framework.serializers import ModelSerializer, CharField

from core.models import ParsedData


class ParsedDataSerializer(ModelSerializer):

    class Meta:
        model = ParsedData
        fields = (
            'id', 'ip_addr', 'log_date',
            'http_method', 'uri', 'error_code',
            'response_size',
        )
