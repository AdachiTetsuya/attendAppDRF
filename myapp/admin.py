from re import S
from django.contrib import admin
from .models import SubmitAttendance,CustomUser
# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)


admin.site.register(SubmitAttendance,RatingAdmin)
admin.site.register(CustomUser)
