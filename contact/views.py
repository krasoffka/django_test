from django.db.models import Q
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from contact.models import Phone
from contact.pagination import DefaultPagination
from contact.serializers import (
    ContactSerializer, OrganisationSerializer, DepartmentSerializer,
    SubdivisionSerializer, PositionSerializer
)
from .models import Contact, Organisation, Department, Subdivision, Position


class OrganisationViewSet(ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    pagination_class = DefaultPagination


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = DefaultPagination


class SubdivisionViewSet(ModelViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer
    pagination_class = DefaultPagination


class PositionViewSet(ModelViewSet):
    serializer_class = PositionSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        qs = Position.objects.all()
        term = self.request.GET.get('term', '').strip()
        if term:
            qs = position_qs_filter_by_term(qs, term)
        return qs


class ContactViewSet(ReadOnlyModelViewSet):
    """
    Contact info.
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    pagination_class = DefaultPagination

    def list(self, request, *args, **kwargs):
        qs = self.queryset
        qs = qs_filter_by_request_param(qs, request)

        page = self.paginate_queryset(qs)
        serializer = self.serializer_class(page, many=True)
        if page is None:
            response = Response(serializer.data)
        else:
            response = self.get_paginated_response(serializer.data)
        return response

    def retrieve(self, request, contact_id=None):
        client = get_object_or_404(self.queryset, id=contact_id)
        serializer = self.serializer_class(client)
        return Response(serializer.data)


def qs_filter_by_request_param(qs, request):
    term = request.GET.get('term', '').strip()
    qs = contact_qs_filter_by_term(qs, term)

    icontains_filter_fields = [
        'first_name', 'last_name', 'patronymic', 'email', 'address', 'office',
        'building'
    ]
    for field_name in icontains_filter_fields:
        value = request.GET.get(field_name, '').strip()
        if value:
            qs = qs_filter_by_param(qs, value, field_name)

    foreign_icontains_filter_fields = [
        'organisation', 'department', 'subdivision', 'position'
    ]
    for field_name in foreign_icontains_filter_fields:
        value = request.GET.get(field_name, '').strip()
        if value:
            qs = qs_filter_foreign_by_param(qs, value, field_name)

    phone_number = request.GET.get('phone', '').strip()
    if phone_number:
        qs = contact_qs_filter_by_phone(qs, phone_number)
    return qs


def contact_qs_filter_by_phone(qs, phone_number):
    phones = Phone.objects.filter(
        contact__in=qs,
        number__icontains=phone_number
    )
    qs = Contact.objects.filter(id__in=[i.contact.id for i in phones])
    return qs


def position_qs_filter_by_term(qs, term):
    return qs.filter(name__icontains=term)


def contact_qs_filter_by_term(qs, term):  # TODO refactor
    search_words = term.split(' ')

    word1 = None
    word2 = None
    try:
        word1 = search_words[0]
        word2 = search_words[1]
    except IndexError:
        pass
    if word1 and not word2:
        qs = qs.filter(
            Q(first_name__icontains=word1) | Q(last_name__icontains=word1)
        )
    elif word2:
        qs = qs.filter(
            (
                Q(first_name__icontains=word1) &
                Q(last_name__icontains=word2)
            )
            |
            (
                Q(first_name__icontains=word2) &
                Q(last_name__icontains=word1)
            )
        )

    return qs


def qs_filter_by_param(qs, param, param_name):
    icontains_filter = {f'{param_name}__icontains': param}
    qs = qs.filter(**icontains_filter)
    return qs


def qs_filter_foreign_by_param(qs, param, param_name):
    print(qs)
    icontains_filter = {f'{param_name}__id': param}
    print(icontains_filter)
    qs = qs.filter(**icontains_filter)
    return qs
