from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUsersForm, RegisterUsersForm


class UsersLoginView(LoginView):
    form_class = LoginUsersForm
    template_name = "login.html"
    extra_context = {"title": "Авторизация"}


class RegisterUsers(CreateView):
    form_class = RegisterUsersForm
    template_name = "register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")
