from rest_framework import serializers
from .models import Category, News, Hashtag


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class HashtagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'