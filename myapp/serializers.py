from dataclasses import field, fields
from rest_framework import serializers
from accounts.models import CustomUser
from .models import SubmitAttendance
from allauth.socialaccount.models import SocialAccount
from rest_framework.serializers import SerializerMethodField
from datetime import date,timedelta
import datetime


class UserSerializer(serializers.ModelSerializer):
    attendances = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username','is_attend','attendances']

    def get_attendances(self,obj):
        yd = datetime.datetime.now()-timedelta(days=1)
        attendances_contents = SubmitAttendance.objects.filter(
            staff=CustomUser.objects.get(id=obj.id),
            time__range=[yd-timedelta(days=7),yd])
        attendances_time = [0] * 7
        for attendances_content in attendances_contents:
            for i in range(7):
                if yd-timedelta(days=i+1)<attendances_content.time<yd-timedelta(days=i):
                    attendances_time[i]+=1
                else:
                    attendances_time[i]+=0
        return attendances_time


class SubmitSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubmitAttendance
        exclude = ('staff',)
        
    def save(self,user):
        is_attend = self.validated_data['is_attend']
        user.is_attend = is_attend
        user.username = SocialAccount.objects.filter(user=user)[0].extra_data['displayName']
        user.save()
        return SubmitAttendance.objects.create(is_attend=is_attend,staff=user)

