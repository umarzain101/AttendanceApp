from django.urls import path, include
from .views import   userAPIView, user_detail, attendanceAPIView, attendance_detail, geologAPIView, geolog_detail
# from .views import user_list, userAPIView, userViewSet, user_detail, attendance_list, attendance_detail, geolog_list, geolog_detail, GenericAPIView


# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('user', userViewSet, basename='user')


urlpatterns = [
    # path('viewset/', include(router.urls)),
    # path('viewset/<str:cnic>/', include(router.urls)),
    # path('user/', user_list),
    path('user/', userAPIView.as_view()),
    path('user_detail/<str:cnic>/', user_detail.as_view()),
    path('attendance/', attendanceAPIView.as_view()),
    path('attendance_detail/<str:cnic>/', attendance_detail.as_view()),
    path('geolog/', geologAPIView.as_view()),
    path('geolog_detail/<str:cnic>/', geolog_detail.as_view()),
    # path('user_detail/<str:cnic>/', user_detail),
    # path('generic/user/<str:cnic>/', GenericAPIView.as_view()),
#     path('attendance/', attendance_list),
#     path('attendance_detail/<str:cnic>/', attendance_detail),
#     path('geolog/', geolog_list),
#     path('geolog_detail/<str:cnic>/', geolog_detail),
]
