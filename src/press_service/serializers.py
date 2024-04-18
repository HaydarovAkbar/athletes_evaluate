from rest_framework import serializers
from .models import News, Image


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
