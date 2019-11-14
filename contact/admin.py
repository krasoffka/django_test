from django.contrib import admin

from .models import (
    Contact, Phone, Organisation, Department, Position, Subdivision,
)


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Contact._meta.fields
        if field.name != "id"
    ]
    fields = [
        field.name for field in Contact._meta.fields
        if field.name != "id"
    ]
    ordering = ('id',)


class PhoneAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Phone._meta.fields
        if field.name != "id"
    ]
    fields = [
        field.name for field in Phone._meta.fields
        if field.name != "id"
    ]
    ordering = ('id',)


class SubdivisionAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Subdivision._meta.fields
        if field.name != "id"
    ]
    fields = [
        field.name for field in Subdivision._meta.fields
        if field.name != "id"
    ]
    ordering = ('id',)


class OrganisationAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Organisation._meta.fields
        if field.name != "id"
    ]
    fields = [
        field.name for field in Organisation._meta.fields
        if field.name != "id"
    ]
    ordering = ('id',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Department._meta.fields
        if field.name != "id"
    ]
    fields = [
        field.name for field in Department._meta.fields
        if field.name != "id"
    ]
    ordering = ('id',)


class PositionAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Position._meta.fields
        if field.name != "id"
    ]
    fields = [
        field.name for field in Position._meta.fields
        if field.name != "id"
    ]
    ordering = ('id',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Subdivision, SubdivisionAdmin)
