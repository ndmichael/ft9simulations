from django.urls import path
from .views import userdashboard, admindashboard, current_user_profile




urlpatterns = [
    path('', current_user_profile, name="currentprofile"),
    path('user/<str:username>', userdashboard , name="userdashboard"),
    path('admin/<str:username>',admindashboard, name="admindashboard")
]