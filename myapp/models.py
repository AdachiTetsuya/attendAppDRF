from django.db import models
from accounts.models import CustomUser

# Create your models here.


class SubmitAttendance(models.Model):

    # 出席か退席か
    is_attend = models.BooleanField(help_text='出席中ならTrue')

    # 誰の
    staff = models.ForeignKey(
        CustomUser,on_delete=models.CASCADE,related_name="staff"
    )
    
    # いつ
    time = models.DateTimeField(auto_now_add=True)


