from rest_framework import serializers
from .models import Category, News, Hashtag


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'is_active')


class HashtagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('id', 'name')


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('uuid', 'title', 'content', 'image', 'published_at', 'hashtag', 'category')

