from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from contact.pagination import DefaultPagination
from test.models import Author


class AuthorSerializer(ModelSerializer):

    class Meta:
        depth = 1
        model = Author
        fields = '__all__'


class AuthorViewSet(ModelViewSet):
    """
    Author info.
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    pagination_class = DefaultPagination

    # def list(self, request, *args, **kwargs):
    #     qs = self.queryset
    #
    #     page = self.paginate_queryset(qs)
    #     serializer = self.serializer_class(page, many=True)
    #     if page is None:
    #         response = Response(serializer.data)
    #     else:
    #         response = self.get_paginated_response(serializer.data)
    #     return response

