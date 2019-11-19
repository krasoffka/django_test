from django.urls import path

from .views import AuthorViewSet

urlpatterns = [
    path('', AuthorViewSet.as_view({'get': 'retrieve'})),
]
