from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import uuid
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = 'categories'


class Hashtag(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return self.name

    abstract = True


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"), null=True)

    image = models.ImageField(upload_to="news/", verbose_name=_("Image"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    published_at = models.DateField(verbose_name=_("Published at"), null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_("UUID"))

    hashtag = models.ManyToManyField(Hashtag, verbose_name=_("Hashtags"), related_name="news")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"), related_name="news")

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return settings.MEDIA_URL + str(self.image)
        return None

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(News, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        db_table = 'news'
        indexes = [
            models.Index(fields=['title', 'created_at']),
        ]
