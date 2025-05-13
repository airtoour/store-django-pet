from typing import List, Dict
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy

from ..forms import AddWomenModelForm
from ..models import Women, TagPosts
from ..utils.mixins import DataMixin

MENU: List[Dict[str, str]] = [
    {
        "title": "О сайте",
        "url_name": "about"
    },
    {
        "title": "Добавить статью",
        "url_name": "add_page"
    },
    {
        "title": "Обратная связь",
        "url_name": "contact"
    },
    {
        "title": "Войти",
        "url_name": "login"
    }
]


class WomenHomeView(DataMixin, ListView):
    """Модель представления Главной страницы"""

    template_name = "index.html"
    context_object_name = "posts"

    title_page = "Главная страница"
    selected = 0

    def get_queryset(self):
        """Получаем список женщин из БД"""
        return Women.published.select_related("category")


class CategoriesView(DataMixin, ListView):
    """Модель представления для категорий на Главной странице"""

    template_name = "index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self):
        """Получаем список категорий из БД по слагу"""
        return (
            Women
            .published
            .filter(category__slug=self.kwargs["category_slug"])
            .select_related("category")
        )

    def get_context_data(self, **kwargs):
        """Метод динамического формирования Категорий на Главной странице"""
        context = super().get_context_data(**kwargs)

        category = context["posts"][0].category

        return self.get_mixin_context(
            context,
            title=f"Категория - {category.name}",
            selected=category.pk
        )


class ShowPostView(DataMixin, DetailView):
    """Модель представления для отображения статьи"""
    template_name = "posts.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        """Метод динамического формирования Деталей поста"""
        context = super().get_context_data(**kwargs)

        return self.get_mixin_context(context, title=context["post"].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


class TagsPostsListView(DataMixin, ListView):
    """Модель представления Тэгов на главной странице"""

    template_name = "index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self):
        return (
            Women.published
            .filter(tags__slug=self.kwargs["tag_slug"])
            .select_related("category")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = TagPosts.objects.get(slug=self.kwargs["tag_slug"])
        return self.get_mixin_context(context, title=f"Тэг: {tag.tag}")
