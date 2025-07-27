from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, ExampleForm  #used for safe user input validation

# Public home view
def home_view(request):
    return HttpResponse("📚 Welcome to the Bookshelf App")
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data securely here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return HttpResponse(f"Form submitted successfully by {name}")
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

# Permission-protected view (basic)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    return HttpResponse("You have permission to view books.")

# Permission-protected view to create a book using a secure form
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # safe against SQL injection via Django ORM
            return redirect('book_list')  # Redirect to book list after creation
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Securely display book list using ORM
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # ORM prevents SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books})
