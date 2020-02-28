from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class PageNumberPagination(pagination.PageNumberPagination):

    # def get_page_size(self, request):
    #     return 10

    def get_paginated_response(self, data):
        current_page = ''
        if self.request.query_params.get('page'):
            str_current_page = str(self.request.query_params.get('page'))
            current_page = int(str_current_page)
        else:
            current_page = 1

        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': current_page,
            'current_url': self.request.build_absolute_uri(self.request.get_full_path()),
            'results': data
        })


class LimitOffSetPagination(pagination.LimitOffsetPagination, pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        current_page = ''
        if self.get_previous_link() is None:
            current_page = 1
        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            limit = int(self.request.query_params.get('limit'))
            offset = int(self.request.query_params.get('offset'))
            current_page = int(offset/limit) + 1
        return Response({
            # 'count': '',
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': '',
            'current_page': str(current_page),
            'current_url': self.request.build_absolute_uri(self.request.get_full_path()),
            'results': data
        })
