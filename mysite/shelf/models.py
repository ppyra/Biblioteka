#coding:utf-8
#kompatybilnośc pythona 3 z 2
from __future__ import unicode_literals, absolute_import, print_function # to musi być zawsze pierwsze (IMPORT Z PRZYSZŁOSCI)
from django.utils.encoding import python_2_unicode_compatible

#from six.moves import range

from django.db import models

@python_2_unicode_compatible # dekorator do starszych wersji python 2
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return "{first_name} {last_name}".format(first_name = self.first_name, last_name=self.last_name)
@python_2_unicode_compatible
class Publiser(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return "{name}".format(name=self.name)
@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publiser, on_delete=models.CASCADE)
    def __str__(self):
        return "{title}".format(title=self.title)