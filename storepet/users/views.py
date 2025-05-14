from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import (
    LoginUsersForm,
    RegisterUsersForm,
    ProfileUsersForm,
    UsersPasswordChangeForm
)
from storepet import settings


class UsersLoginView(LoginView):
    form_class = LoginUsersForm
    template_name = "login.html"
    extra_context = {"title": "Авторизация"}


class RegisterUsers(CreateView):
    form_class = RegisterUsersForm
    template_name = "register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")


class ProfileUsersView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUsersForm
    template_name = "profile.html"
    extra_context = {
        "title": "Профиль пользователя",
        "default_image": settings.DEFAULT_USER_IMAGE
    }

    def get_success_url(self):
        return reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class UsersPasswordChangeView(PasswordChangeView):
    form_class = UsersPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "password_change_form.html"
