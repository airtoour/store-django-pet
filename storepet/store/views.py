from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': True},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

categories_db = [
    {"id": 1, "name": "Актрисы"},
    {"id": 2, "name": "Певицы"},
    {"id": 3, "name": "Спортсменки"},
]

def index(request: HttpRequest):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'selected': 0
    }
    return render(request, 'index.html', context=data)


def about(request: HttpRequest):
    return render(request, 'about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request: HttpRequest, post_id: int):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


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
