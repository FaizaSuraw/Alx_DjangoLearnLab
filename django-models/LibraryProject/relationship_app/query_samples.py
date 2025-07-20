import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ✅ Query all books by a specific author using filter()
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# ✅ List all books in a library (this is okay as is)
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# ✅ Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Example usage (can be run with: python query_samples.py)
if __name__ == '__main__':
    print("Books by Jane Austen:", books_by_author("Jane Austen"))
    print("Books in Central Library:", books_in_library("Central Library"))
    print("Librarian for Central Library:", librarian_for_library("Central Library"))
