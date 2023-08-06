from rest_framework import serializers
from MangoRead.models import MangaCard, Review


class ReviewSerializer(serializers.ModelSerializer):
    # manga = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    text = serializers.CharField(required=True)

    class Meta:
        model = Review
        fields = 'id manga author author_user text'.split()


class MangaCardsSerializer(serializers.ModelSerializer):
    manga_review = ReviewSerializer(many=True, required=False)

    class Meta:
        model = MangaCard
        fields = ' id photo name type year genre synopsis manga_review'.split()
