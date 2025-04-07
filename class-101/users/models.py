import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import UUIDModel, SoftDeletableModel


class User(UUIDModel, AbstractBaseUser, SoftDeletableModel):
    email = models.EmailField(_('email address'))
    password = models.CharField(_('password'), max_length=128, null=True, blank=True)
