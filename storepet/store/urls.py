from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),

    path("about/", views.about, name="about"),
    path("add_page/", views.add_page, name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),

    path("posts/<slug:post_slug>/", views.show_post, name="posts"),

    path("categories/<slug:category_slug>/", views.show_categories, name="categories"),
    path("tags/<slug:tag_slug>", views.show_tag_posts_list, name="tags")
]
