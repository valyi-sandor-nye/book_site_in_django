from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    is_female = models.BooleanField()

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_available = models.BooleanField()

    def __str__(self):
        return f'{self.author}: {self.title}'
