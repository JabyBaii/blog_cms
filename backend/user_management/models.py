from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 添加额外字段
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)