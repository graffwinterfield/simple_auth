from datetime import datetime
from datetime import timedelta

from cffi.backend_ctypes import unicode
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import jwt
from django.conf import settings

import json


class User(AbstractUser):
    verification_code = models.CharField(max_length=20, null=True)


#    objects = UserManager()

class Maps(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='maps')
    maps = models.JSONField(max_length=200)

