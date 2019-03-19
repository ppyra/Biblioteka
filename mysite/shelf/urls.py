from django.contrib import admin
from django.urls import path

from .views import AuthorDetailView, AuthorListView, BookListView

urlpatterns = [
path('authors/', AuthorListView.as_view(), name='author-list'),
path('authors/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
path('ksiazki/', BookListView.as_view(), name='book-list'),
]