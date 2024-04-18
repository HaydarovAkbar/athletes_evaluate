from django.contrib import admin
from .models import Category, Hashtag, News


admin.site.register(Category)
admin.site.register(Hashtag)
admin.site.register(News)

