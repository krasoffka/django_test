"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from contact.views import (
    OrganisationViewSet, DepartmentViewSet, SubdivisionViewSet, PositionViewSet
)

router = routers.DefaultRouter()
router.register(r'organisations', OrganisationViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'subdivisions', SubdivisionViewSet)
router.register(r'positions', PositionViewSet, basename='Position')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('test/', include('test.api.urls')),
    path('', include(router.urls)),
]
