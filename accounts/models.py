from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'

    # 出席中か
    is_attend = models.BooleanField(default=False,help_text='出席中ならTrue')