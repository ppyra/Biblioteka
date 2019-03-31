#coding:utf-8
from __future__ import unicode_literals, absolute_import, print_function # to musi być zawsze pierwsze (IMPORT Z PRZYSZŁOSCI)
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
#from six.moves import range

from django.db import models
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible # dekorator do starszych wersji python 2
class Author(models.Model):
    first_name = models.CharField(verbose_name= _("first_name") ,max_length=20)
    last_name = models.CharField(_("last_name"), max_length=50)

    def __str__(self):
        return _("{first_name} {last_name}").format(first_name = self.first_name, last_name=self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name') # w jakis sposób beda dane sortowane w bazie
        verbose_name = _('author') # nazwa modelu, gdy wystepuje w liczbie pojedyńczej
        verbose_name_plural = _('authors') # nazwa modelu, gdy wystepuje w liczbie mnogiej

@python_2_unicode_compatible
class Publiser(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return "{name}".format(name=self.name)

@python_2_unicode_compatible
class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Book(models.Model):
    "coś w rodzaju rękopisu"

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categtegories = models.ManyToManyField(BookCategory)
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "{title}".format(title=self.title)

# Zwraca ścieżkę szczegółów dostępu do danego modlu
    def get_absolute_url(self):
        #reverse zamienia nazwę widoku, podając parametry na konkretną ścieżkę
        return reverse('shelf:book-detail', kwargs={'pk':self.id})


@python_2_unicode_compatible
class BookEdition(models.Model):
    "wydanie określonej ksiażeki"
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='editions')
    isbn = models.CharField(max_length=17, blank=True) #blank=True moze zawierać null
    date = models.DateField()
    publisher = models.ForeignKey(Publiser, on_delete=models.CASCADE)

    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book, publisher=self.publisher)
COVER_TYPES = {
    ('soft', 'Soft'),
    ('hard', "Hard"),
    #wartość przechowywana w bazie , wartść wyświetlana
}

@python_2_unicode_compatible
class BookItem(models.Model):
    "konkretny egzemplarz"
    edition = models.ForeignKey(BookEdition, on_delete=models.CASCADE)
    catalog_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    def __str__(self):
        return "{edition},{cover}".format(edition=self.edition, cover=self.get_cover_display())