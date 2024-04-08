from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class Competition(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Competition")
        verbose_name_plural = _("Competitions")
        db_table = 'competition'
        indexes = [
            models.Index(fields=['title', 'is_active']),
        ]

    def __str__(self):
        return self.title


class Ring(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True, verbose_name=_("Competition"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Ring")
        verbose_name_plural = _("Rings")
        db_table = 'ring'
        indexes = [
            models.Index(fields=['title', 'is_active']),
            models.Index(fields=['competition']),
        ]

    def __str__(self):
        return self.title