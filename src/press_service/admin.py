from django.contrib import admin
from .models import News
from .models import Image

# Register your models here.

admin.site.register(News)
admin.site.register(Image)

