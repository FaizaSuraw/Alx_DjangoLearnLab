from django.urls import path
from .views import home_view, view_books, create_book
from .views import book_list

urlpatterns = [
    path('', home_view, name='bookshelf-home'),
    path('view/', view_books, name='view-books'),
    path('create/', create_book, name='create-book'),
    path('books/', book_list, name='book_list'),
]
