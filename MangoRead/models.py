from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MangaCard(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, related_name='manga_type', on_delete=models.PROTECT)
    year = models.IntegerField()
    genre = models.ManyToManyField(Genre, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    manga = models.ForeignKey(MangaCard, on_delete=models.CASCADE, related_name='manga_review')

    def __str__(self):
        return self.text


