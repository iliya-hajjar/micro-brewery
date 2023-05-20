from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class User(AbstractUser):
    activation_code = models.UUIDField(unique=True, default=uuid4, editable=False)
