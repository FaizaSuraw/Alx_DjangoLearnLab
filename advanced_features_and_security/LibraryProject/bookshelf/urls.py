from django.urls import path
from .views import home_view, view_books, create_book

urlpatterns = [
    path('', home_view, name='bookshelf-home'),
    path('view/', view_books, name='view-books'),
    path('create/', create_book, name='create-book'),
]
