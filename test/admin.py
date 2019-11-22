from django.contrib import admin


# Register your models here.
from test.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'get_friends']
    fields = ['id', 'name', 'age', 'friends']
    ordering = ('id',)
    readonly_fields = ('id', )

    def get_friends(self, obj):
        return "\n".join([p.name for p in obj.friends.all()])


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']
    fields = ['id', 'name', 'author']
    ordering = ('id',)
    readonly_fields = ('id', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
