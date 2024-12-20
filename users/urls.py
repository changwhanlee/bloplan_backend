from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.UserSignUp.as_view()),
    path('me', views.Me.as_view()),
    path('change-password', views.ChangePassword.as_view()),
    path('log-in', views.LogIn.as_view()),
    path('log-out', views.LogOut.as_view()),
    path('check-username', views.CheckUserName.as_view()),
]   
