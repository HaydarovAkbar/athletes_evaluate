from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from account.models import User
import uuid


class Competition(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_("User"))
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name = _("Musobaqa")
        verbose_name_plural = _("Musobaqalar")
        db_table = 'competition'
        indexes = [
            models.Index(fields=['title', 'is_active']),
        ]

    def __str__(self):
        return self.title


class Ring(models.Model):
    title = models.CharField(max_length=20, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, related_name="ring", null=True,
                                    verbose_name=_("Competition"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Ring")
        verbose_name_plural = _("Ringes")
        db_table = 'ring'
        indexes = [
            models.Index(fields=['is_active']),
            models.Index(fields=['competition']),
        ]

    def __str__(self):
        return f"Ring for {self.competition.title}"


class Match(models.Model):
    user1 = models.CharField(max_length=150, null=True, verbose_name=_('raqib 1'))
    user2 = models.CharField(max_length=150, null=True, verbose_name=_('raqib 2'))
    ring = models.ForeignKey(Ring, on_delete=models.SET_NULL, null=True)
    result = models.PositiveIntegerField(null=True)

    is_finished = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matchs")
        db_table = 'match'
        indexes = [
            models.Index(fields=['is_finished']),
            models.Index(fields=['ring']),
        ]

    def __str__(self):
        return str(self.created_at)


class MatchResult(models.Model):
    ko_choice = (
        (1, 'user1'),
        (2, 'user2'),
    )

    user1_point = models.CharField(max_length=500, null=True)
    user2_point = models.CharField(max_length=500, null=True)
    match = models.OneToOneField(Match, on_delete=models.SET_NULL, null=True)
    referee = models.OneToOneField(User, related_name='match_result', on_delete=models.SET_NULL, null=True)
    total_point1 = models.PositiveIntegerField(null=True)
    total_point2 = models.PositiveIntegerField(null=True)

    is_finished = models.BooleanField(default=False)

    knock_out = models.CharField(max_length=10, choices=ko_choice, null=True, blank=True)

    class Meta:
        verbose_name = 'match_result'
        verbose_name_plural = 'match_results'
        db_table = 'match_result'

    def __str__(self):
        return f"{self.match.user1} vs {self.match.user2}'s result"
