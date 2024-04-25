from rest_framework import serializers

from .models import Category, News, Hashtag


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('uuid', 'title', 'content', 'image', 'published_at', 'hashtag', 'category')


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class HashtagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('id', 'name',)
