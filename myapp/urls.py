from django.urls import path,include

from rest_framework import routers
from myapp.views import *

router = routers.DefaultRouter()
router.register('attendpost',AttendViewSet)



urlpatterns = [
    path("createsubmit/",SubmitAPI.as_view()),
    path("userList/",UserListView.as_view()),
    path('staff/<int:pk>/', UserDetailAPIView.as_view(), name='detail'),
]

urlpatterns += router.urls