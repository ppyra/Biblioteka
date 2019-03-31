from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Author, Book
from django.views import View
from django.http import HttpResponse

class MainPageView(TemplateView):
   template_name = 'index.html'
   # def get(self, request, *args, **kwargs):
    #    return HttpResponse('OK-klasa')

#index_view = MainPageView.as_view()

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book