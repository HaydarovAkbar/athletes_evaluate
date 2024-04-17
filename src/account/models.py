from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField

from app.models import Ring

import uuid

def password_validator(value):
    pass 

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
    updated_at = models.DateTimeField(auto_now=True, null=True)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = 'account_user'
        indexes = [
            models.Index(fields=['username', 'phone_number', 'email']),
        ]


class RefereeUser(AbstractUser):
    ring = models.ForeignKey(Ring, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Ring'))
    main = models.BooleanField(default=False)
    is_referee = models.BooleanField(default=True)
    username = models.CharField(max_length=100, validators=[RegexValidator(regex=r"^[1-9 a-z]+$",
                                                                                      message="Enter a valid username in the format sdfsf7654",
                                                                                      code="invalid_username", )])
    password = models.PositiveBigIntegerField(validators=[RegexValidator(regex=r"^[1-9]+$",
                                                                         message="Enter a valid password in the format 1234567654",
                                                                         code="invalid_password", )])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    USERNAME_FIELD = "username"
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="%(app_label)s_%(class)s_related",  # Change the related_name
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_related",  # Change the related_name
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        verbose_name = 'Hakam'
        verbose_name_plural = 'Hakamlar'
        db_table = 'referee_user'
        indexes = [
            models.Index(fields=['ring']),
        ]
