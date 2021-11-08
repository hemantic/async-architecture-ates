from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as _UserManager
from django.db import models


class UserManager(_UserManager):
    pass


class User(AbstractUser):
    objects = UserManager()

    REQUIRED_FIELDS = []
