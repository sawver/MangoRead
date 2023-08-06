from rest_framework import viewsets, generics, permissions
from rest_framework.filters import SearchFilter
from MangoRead import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MangaFilter
from .paginations import MangaCardsPagination


class MangaCardsAPIViewSet(viewsets.ModelViewSet):
    queryset = models.MangaCard.objects.all()
    serializer_class = serializers.MangaCardsSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_class = MangaFilter
    search_fields = ['name']
    pagination_class = MangaCardsPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'


class AddReviewView(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
