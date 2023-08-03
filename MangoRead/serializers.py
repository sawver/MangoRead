from rest_framework import serializers
from MangoRead.models import MangaCard


class MangaCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaCard
        fields = '__all__'
