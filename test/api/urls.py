from django.urls import path
from rest_framework.routers import DefaultRouter

from test.api.views import BookViewSet
from .views import AuthorViewSet


router = DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'author', BookViewSet)


urlpatterns = [
    # path('author/', AuthorViewSet.as_view({'get': 'list'})),
]

urlpatterns += router.urls
