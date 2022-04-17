from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'

    # 出席中か
    is_attend = models.BooleanField(default=False,help_text='出席中ならTrue')


class SubmitAttendance(models.Model):

    # 出席か退席か
    is_attend = models.BooleanField(help_text='出席中ならTrue')

    # 誰の
    staff = models.ForeignKey(
        CustomUser,on_delete=models.CASCADE,related_name="staff"
    )
    
    # いつ
    time = models.DateTimeField(auto_now_add=True)


