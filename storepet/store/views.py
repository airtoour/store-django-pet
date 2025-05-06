from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render, get_object_or_404

from .models.women import Women


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

categories_db = [
    {"id": 1, "name": "Актрисы"},
    {"id": 2, "name": "Певицы"},
    {"id": 3, "name": "Спортсменки"},
]

def index(request: HttpRequest):
    posts = Women.objects.filter(is_published=1)

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'selected': 0
    }
    return render(request, 'index.html', context=data)


def about(request: HttpRequest):
    return render(request, 'about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request: HttpRequest, post_slug: str):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "selected": 1
    }

    return render(request, "post.html", data)


def addpage(request: HttpRequest):
    return HttpResponse("Добавление статьи")


def contact(request: HttpRequest):
    return HttpResponse("Обратная связь")


def login(request: HttpRequest):
    return HttpResponse("Авторизация")


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_categories(request: HttpRequest, category_id: int):
    data = {
        'title': 'Рубрика',
        'menu': menu,
        'posts': data_db,
        'selected': category_id
    }
    return render(request, 'index.html', context=data)
