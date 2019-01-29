from rest_framework import pagination
from django.db.models import Sum, Count, Q

from ...models import ParsedData


class PaginationWithAggregates(pagination.LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        # перегружаем пагинацию для /api/v1/parsed_data/

        if request._request.path == '/api/v1/parsed_data/':
            self.unique_ip_count = queryset.aggregate(
                count_ip=Count('ip_addr', distinct=True))['count_ip']
            self.top_ten_ip = queryset.annotate(freq=Count('ip_addr')).\
                order_by('-freq')[0:10].values('ip_addr', 'freq')
            self.GET_count = queryset.filter(http_method='GET').count()
            self.POST_count = queryset.filter(http_method='POST').count()
            self.total_transfered_bytes = queryset.\
                aggregate(total=Sum('response_size'))['total']
        return super(PaginationWithAggregates, self).paginate_queryset(
            queryset, request, view
        )

    def get_paginated_response(self, data):
        paginated_response = super(PaginationWithAggregates, self)\
            .get_paginated_response(data)

        if self.request._request.path == '/api/v1/parsed_data/':
            paginated_response.data['statistics'] = {
                'unique_ip_count': self.unique_ip_count,
                'top_ten_ip': self.top_ten_ip,
                'GET_count': self.GET_count,
                'POST_count': self.POST_count,
                'total_transfered_bytes': self.total_transfered_bytes,
            }
        return paginated_response
