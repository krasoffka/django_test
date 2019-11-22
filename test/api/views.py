from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from contact.pagination import DefaultPagination
from test.api.serializers import AuthorSerializer
from test.models import Author, Book


class AuthorViewSet(ModelViewSet):
    """
    Author info.
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    pagination_class = DefaultPagination
    lookup_field = 'pk'


class BookDetailSerializer(ModelSerializer):

    class Meta:
        depth = 1
        model = Book
        fields = '__all__'


class BookSerializer(ModelSerializer):

    class Meta:
        depth = 1
        model = Book
        fields = '__all__'


class BookListSerializer(ModelSerializer):

    class Meta:
        depth = 1
        model = Book
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    id = serializers.ModelField(model_field=Author()._meta.get_field('id'))

    class Meta:
        # depth = 1
        model = Author
        fields = '__all__'


class BookCreateSerializer(ModelSerializer):
    # id = serializers.ModelField(model_field=Book()._meta.get_field('id'))
    author = AuthorSerializer()
    # author = serializers.IntegerField()

    class Meta:
        depth = 1
        model = Book
        fields = ('name', 'author')

    def update(self, instance, validated_data):
        print(validated_data)
        return instance

    def create(self, validated_data):
        print(validated_data)
        author = AuthorSerializer(data=validated_data.get('author'))
        author.is_valid()
        instance = author.save()
        print(instance.id)
        author = Author.objects.get(id=3)
        book = Book.objects.create(name=validated_data['name'], author=instance)
        return book


class BookViewSet(ModelViewSet):
    """
    Book info.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = DefaultPagination
    lookup_field = 'pk'

    action_serializers = {
        'retrieve': BookDetailSerializer,
        'list': BookListSerializer,
        'create': BookCreateSerializer,
        'partial_update': BookCreateSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            print('Ser')
            print(self.action)
            return self.action_serializers.get(
                self.action,
                self.serializer_class
            )
        print(1111)
        return super(BookViewSet, self).get_serializer_class()
