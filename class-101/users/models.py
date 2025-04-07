import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import UUIDModel, SoftDeletableModel


class User(UUIDModel, AbstractUser, SoftDeletableModel):
    user_id = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(_('password'), max_length=128, null=True, blank=True)
    EMAIL_FIELD = None
    USERNAME_FIELD = 'username'
    email = None
    first_name = None
    last_name = None
    REQUIRED_FIELDS = []