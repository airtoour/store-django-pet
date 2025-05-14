from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, DeleteView

from ..forms import AddWomenModelForm
from ..models import Women
from ..utils.mixins import DataMixin
from ..utils.base_mappings import MENU


def add_page(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddWomenModelForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                return redirect("home")
            except Exception as e:
                form.add_error(None, "Ошибка добавления поста")
                print(e)
    else:
        form = AddWomenModelForm()

    data = {
        "title": "Добавить статью",
        "menu": MENU,
        "form": form
    }

    return render(request, template_name="add_page.html", context=data)


class PagesAddView(View):
    """
    Модель представления добавления
    новой статьи через базовый класс View
    """

    def get(self, request):
        """HTTP Метод получения формы"""
        form = AddWomenModelForm()

        data = {
            "title": "Добавить статью",
            "menu": MENU,
            "form": form
        }

        return render(request, template_name="add_page.html", context=data)

    def post(self, request):
        """HTTP Метод сохранения данных из формы в БД"""
        form = AddWomenModelForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                return redirect("home")
            except Exception as e:
                form.add_error(None, "Ошибка добавления поста")
                print(e)

        data = {
            "title": "Добавить статью",
            "menu": MENU,
            "form": form
        }

        return render(request, template_name="add_page.html", context=data)


class PagesAddFormView(FormView):
    """
    Модель представления добавления
    новой статьи через класс FormView
    """

    form_class = AddWomenModelForm
    template_name = "add_page.html"
    success_url = reverse_lazy("home")

    extra_context = {
        "menu": MENU,
        "title": "Добавление статьи"
    }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PagesCreateView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    """
    Модель представления добавления
    новой статьи через класс CreateView
    """

    form_class = AddWomenModelForm
    template_name = "add_page.html"

    title_page = "Добавление статьи"

    permission_required = "store.add_women"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user

        return super().form_valid(form)


class PagesUpdateView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    """
    Модель представления обновления
    новой статьи через класс CreateView
    """

    model = Women
    fields = ["title", "content", "photo", "is_published", "category"]
    template_name = "add_page.html"
    success_url = reverse_lazy("home")

    title_page = "Редактирование статьи"

    permission_required = "store.change_women"


class PagesDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DeleteView):
    """
    Модель представления удаления
    новой статьи через класс CreateView
    """

    model = Women
    template_name = "add_page.html"
    success_url = reverse_lazy("home")

    title_page = "Удаление статьи"
