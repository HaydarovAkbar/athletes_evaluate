from django.contrib import admin
from .models import Category, Hashtag, News

admin.site.register(News)
admin.site.register(Hashtag)
admin.site.register(Category)
