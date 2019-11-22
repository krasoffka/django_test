from rest_framework.serializers import ModelSerializer

from test.models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):

    class Meta:
        depth = 1
        model = Book
        fields = '__all__'
