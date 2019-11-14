from rest_framework import serializers

from contact.models import Phone, Position, Subdivision, Department, \
    Organisation
from .models import Contact


class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class SubdivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subdivision
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'name', 'number')


class ContactSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(source='phones', many=True)

    class Meta:
        depth = 1
        model = Contact
        fields = '__all__'
