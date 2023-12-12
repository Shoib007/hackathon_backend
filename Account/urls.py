from django.urls import path
from .views.userView import UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    path('login/', UserLoginView, name="UserLoginView"),
    path('register/', UserRegisterView, name="UserRegisterView"),
    path('logout/', UserLogoutView, name="LogoutView"),
]