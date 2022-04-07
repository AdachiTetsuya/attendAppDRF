from distutils.log import error
from allauth.socialaccount.providers.line.views import LineOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import viewsets,mixins
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.response import Response
from .models import SubmitAttendance
from rest_framework.views import APIView
from django.db.models import OuterRef,Subquery
from rest_framework.generics import RetrieveAPIView
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import formats
from django.conf import settings

User = get_user_model()

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class LineLogin(SocialLoginView):
    adapter_class = LineOAuth2Adapter
    client_class = OAuth2Client
    callback_url = f"{settings.ATTEND_FRONT_ROOT}/callback/"
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'



class AttendViewSet(viewsets.ModelViewSet):
    queryset = SubmitAttendance.objects.all()
    serializer_class = SubmitSerializer


# 出席履歴の保存
class SubmitAPI(APIView):
    def post(self, request):
        user = request.user
        serializer = SubmitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user)
            return Response(serializer.data)
        else:
            return Response(error)


# ユーザー一覧
class UserListView(APIView):
    def get(self, request):
        # ユーザーひとりずつの最新の出席履歴
        latest_attend = SubmitAttendance.objects.filter(
            staff=OuterRef("pk")
        ).order_by("-time")
        
        users = User.objects.all().annotate(
            latest_attend_pk=Subquery(latest_attend.values("pk")[:1]),
            latest_attend_time=Subquery(latest_attend.values("time")[:1]),
        ).order_by("-latest_attend_pk")

        res_list = [
            {
                'id':user.id,
                'username':user.username,
                'is_attend':user.is_attend,
                'time':formats.date_format(user.latest_attend_time,"(H:i~)"),

            }
            for user in users if user.latest_attend_time
        ]
        return Response(res_list)

            


