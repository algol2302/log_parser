from django_filters import rest_framework as django_filters

from ...models import ParsedData


class ParsedDataFilter(django_filters.FilterSet):

    class Meta:
        model = ParsedData
        fields = ('__all__')
