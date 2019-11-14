from rest_framework.pagination import PageNumberPagination, \
    LimitOffsetPagination


class ContactPageNumberPagination(PageNumberPagination):
    page_size = 100


class DefaultPagination(LimitOffsetPagination):
    default_limit = 10
