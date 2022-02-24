from rest_framework import serializers
from accounts.models import CustomUser
from .models import SubmitAttendance
from allauth.socialaccount.models import SocialAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','is_attend']

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

