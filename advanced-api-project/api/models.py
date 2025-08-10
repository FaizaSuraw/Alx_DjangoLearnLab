from django.db import models

# Author model to store writer details
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's full name

    def __str__(self):
        return self.name


# Book model with a ForeignKey to Author (One-to-Many)
class Book(models.Model):
    title = models.CharField(max_length=255)          # Book title
    publication_year = models.IntegerField()          # Year published
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
