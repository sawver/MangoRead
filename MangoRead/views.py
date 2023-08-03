from rest_framework import viewsets
from MangoRead import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MangaFilter
from .paginations import MangaCardsPagination


class MangaCardsAPIViewSet(viewsets.ModelViewSet):
    queryset = models.MangaCard.objects.all()
    serializer_class = serializers.MangaCardsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MangaFilter
    pagination_class = MangaCardsPagination
    lookup_field = 'id'
