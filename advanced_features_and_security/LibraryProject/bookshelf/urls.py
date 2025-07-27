from django.urls import path
from .views import home_view, view_books, create_book, example_form_view, book_list

urlpatterns = [
    path('', home_view, name='bookshelf-home'),
    path('view/', view_books, name='view-books'),
    path('create/', create_book, name='create-book'),
    path('books/', book_list, name='book_list'),
    path('example-form/', example_form_view, name='example_form'),
]
