from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def home_view(request):
    return HttpResponse("📚 Welcome to the Bookshelf App")

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    return HttpResponse("You have permission to view books.")

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("You have permission to create a book.")

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
