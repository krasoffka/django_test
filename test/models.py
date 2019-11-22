from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    friends = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Book(models.Model):
    name = models.CharField(max_length=16)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
