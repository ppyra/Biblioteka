from django.contrib import admin

from .models import Author, Publiser, Book

admin.site.register([Author, Publiser, Book]) #dodaje do panelu admina tabele z bazą danych

