from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MangaCard(models.Model):
    photo = models.ImageField(blank=True, upload_to="media", verbose_name="Фото")
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

    def __str__(self):
        return self.text
