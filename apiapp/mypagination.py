from rest_framework.pagination import LimitOffsetPagination

class MyPaginationClass(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 7
    