from django.db import models
from author.models import Author

class Book(models.Model):
    name = models.CharField(max_length=150, blank=False)
    edition = models.CharField(max_length=5, blank=False)
    publication_year= models.CharField(max_length=4, blank=False)
    authors =  models.ManyToManyField(Author, blank=True)

    def __str__(self):
        return self.name
