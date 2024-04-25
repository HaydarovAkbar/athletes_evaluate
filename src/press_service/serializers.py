from rest_framework import serializers

from .models import Category, News, Hashtag


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'content', 'image', 'published_at', 'uuid', 'hashtag', 'category')


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class HashtagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('name',)
