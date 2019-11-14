from django.urls import path

from .views import ContactViewSet

urlpatterns = [
    path('', ContactViewSet.as_view({'get': 'list'})),
    path('<int:contact_id>', ContactViewSet.as_view({'get': 'retrieve'})),
]
