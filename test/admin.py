from django.contrib import admin


# Register your models here.
from test.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_friends']
    fields = ['id', 'name', 'friends']
    ordering = ('id',)
    readonly_fields = ('id', )

    def get_friends(self, obj):
        return "\n".join([p.name for p in obj.friends.all()])


admin.site.register(Author, AuthorAdmin)
