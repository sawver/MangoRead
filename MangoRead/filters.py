from django_filters import rest_framework as filters
from .models import Type, Genre, MangaCard


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MangaFilter(filters.FilterSet):
    type = filters.ModelChoiceFilter(queryset=Type.objects.filter())
    genre = filters.ModelMultipleChoiceFilter(queryset=Genre.objects.filter())
    year = filters.RangeFilter()

    class Meta:
        model = MangaCard
        fields = ['genre', 'year', 'type']
