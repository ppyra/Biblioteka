from django.contrib import admin

from .models import (
    Author, Publiser, Book, BookCategory, BookEdition, BookItem,
)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name'] # dodaje wyszukiwarkę
    ordering = ['last_name'] # sortowanie

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register([Publiser]) #dodaje do panelu admina tabele z bazą danych
admin.site.register(BookCategory)
admin.site.register(BookEdition)
admin.site.register(BookItem)
