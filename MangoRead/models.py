from django.db import models
from users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MangaCard(models.Model):
    photo = models.ImageField(upload_to="media", verbose_name="Фото", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    type = models.ForeignKey(Type, related_name='manga_type', on_delete=models.PROTECT, verbose_name="Тип")
    year = models.PositiveSmallIntegerField(verbose_name="Год")
    genre = models.ManyToManyField(Genre, blank=True, verbose_name="Жанр")
    synopsis = models.TextField(blank=True, null=True, verbose_name="Синопсис")

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    manga = models.ForeignKey(MangaCard, on_delete=models.CASCADE, related_name='manga_review')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')

    def __str__(self):
        return self.text

    def author_user(self):
        return [self.author.username, self.author.nickname]
