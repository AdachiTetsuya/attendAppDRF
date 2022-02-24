from django.urls import path,include

from rest_framework import routers
from myapp.views import HomeViewSet,AttendViewSet,SubmitAPI,UserListView

router = routers.DefaultRouter()
router.register('home',HomeViewSet)
router.register('attendpost',AttendViewSet)



urlpatterns = [
    path("createsubmit/",SubmitAPI.as_view()),
    path("userList/",UserListView.as_view()),
]

urlpatterns += router.urls