from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField

import uuid


class User(AbstractUser):
    phone_number = PhoneNumberField(
        _("Phone number"),
        help_text=_("Required. Only international format used. (+998901234567)"),
        error_messages={
            "unique": _("User this phone number already exists.")
        },
        unique=True,
        blank=True,
        null=True, )
    ring = models.ForeignKey('app.Ring', on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=6, unique=True, validators=[RegexValidator(regex=r"^[1-9 a-z]+$",
                                                                                      message="Enter a valid username in the format sdfsf7654",
                                                                                      code="invalid_username", )])
    password = models.CharField(max_length=255)

    updated_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Updated At"))
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if self.password:
            self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = 'account_user'
        indexes = [
            models.Index(fields=['username', 'phone_number', 'email']),
        ]
