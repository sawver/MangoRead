from django.contrib import admin
from MangoRead.models import Type, Genre, MangaCard, Review

# Register your models here.

admin.site.register(Type)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(MangaCard)
