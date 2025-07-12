\# CRUD Operations Summary



\## Create

```python

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book = Book.objects.get(id=1)


book.title = "Nineteen Eighty-Four"
book.save()

book.delete()



