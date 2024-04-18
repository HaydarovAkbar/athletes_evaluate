from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import uuid
from django.utils import timezone

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to="images/", verbose_name=_("Image"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        return self.image.url

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        return self

    def get_image_url(self):
        return settings.HOST + self.image.url

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        db_table = 'images'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"), null=True)

    image = models.ForeignKey(Image, on_delete=models.SET_NULL, verbose_name=_("Image"), null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    published_at = models.DateField(verbose_name=_("Published at"), null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_("UUID"))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        db_table = 'news'
        indexes = [
            models.Index(fields=['title', 'created_at']),
        ]
