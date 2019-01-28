from rest_framework import pagination
from django.db.models import Sum, Count, Q

from ...models import ParsedData


class PaginationWithAggregates(pagination.LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        # перегружаем пагинацию для /api/v1/parsed_data/

        if request._request.path == '/api/v1/parsed_data/':
            self.unique_ip_count = queryset.count()
            self.top_ten_ip = 0
            self.GET_count = 0
            self.POST_count = 0
            self.total_transfered_bytes = 0
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
