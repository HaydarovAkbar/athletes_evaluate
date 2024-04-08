from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser, Group
from phonenumber_field.modelfields import PhoneNumberField

import uuid


class User(AbstractUser):
    phone_number = PhoneNumberField(
        _("Phone number"),
        help_text=_("Required. Only international format used. (998901234567)"),
        error_messages={
            "unique": _("User this phone number already exists.")
        },
        unique=True,
        blank=True,
        null=True, )
    updated_at = models.DateTimeField(auto_now=True, null=True)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    group = models.ManyToManyField(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = 'account_user'
        indexes = [
            models.Index(fields=['username', 'phone_number', 'email']),
        ]