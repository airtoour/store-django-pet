from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddWomenModelForm, UploadFilesForm
from .models import Categories, Women, TagPosts, Files
from .services.files import handle_upload_file


menu = [
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


def index(request: HttpRequest):
    posts = Women.objects.filter(is_published=1).select_related("category")

    data = {
        "title": "Главная страница",
        "menu": menu,
        "posts": posts,
        "selected": 0
    }

    return render(request, template_name="index.html", context=data)


def show_post(request: HttpRequest, post_slug: str):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "selected": 1
    }

    return render(request, template_name="posts.html", context=data)


def show_categories(request: HttpRequest, category_slug: str):
    category = get_object_or_404(Categories, slug=category_slug)
    posts = Women.objects.filter(category_id=category.pk).select_related("category")

    data = {
        "title": f"Рубрика: {category.name}",
        "menu": menu,
        "posts": posts,
        "selected": category.pk
    }

    return render(request, template_name="index.html", context=data)

def show_tag_posts_list(request: HttpRequest, tag_slug: str):
    tag = get_object_or_404(TagPosts, slug=tag_slug)
    posts = (
        tag.tags
        .filter(is_published=Women.Status.PUBLISHED)
        .select_related("category")
    )

    data = {
        "title": f"Тэг: {tag}",
        "menu": menu,
        "posts": posts,
        "selected": None
    }

    return render(request, template_name="index.html", context=data)


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
        "menu": menu,
        "form": form
    }

    return render(request, template_name="add_page.html", context=data)


def contact(request: HttpRequest) -> HttpResponse:
    data = {"title": "Обратная связь", "menu": menu}

    return render(request, template_name="contact.html", context=data)


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Авторизация")


def about(request: HttpRequest):
    if request.method == "POST":
        form = UploadFilesForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = Files(file=request.FILES["file"])
            uploaded_file.save()
    else:
        form = UploadFilesForm()

    data = {"title": "О сайте", "menu": menu, "form": form}

    return render(request, template_name="about.html", context=data)


def page_not_found(request: HttpRequest, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
