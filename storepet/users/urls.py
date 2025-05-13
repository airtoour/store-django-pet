from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


app_name = "users"

urlpatterns = [
    path("login/", views.UsersLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterUsers.as_view(), name="register")
]
