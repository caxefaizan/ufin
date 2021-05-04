from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    uuid = models.CharField(max_length=200)
    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(max_length=200)
    uuid = models.CharField(max_length=200, primary_key = True)
    description = models.CharField(max_length=200)
    movie = models.ManyToManyField(Movie)


    def __str__(self): 
        return self.title







