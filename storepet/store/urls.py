from django.urls import path
from . import views


urlpatterns = [
    path("", views.WomenHomeView.as_view(), name="home"),

    path("about/", views.about, name="about"),

    path("pages/add/", views.PagesCreateView.as_view(), name="add_page"),
    path("pages/edit/<slug:slug>", views.PagesUpdateView.as_view(), name="edit_page"),
    path("pages/delete/<slug:slug>", views.PagesDeleteView.as_view(), name="delete_page"),

    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),

    path("posts/<slug:post_slug>/", views.ShowPostView.as_view(), name="posts"),

    path("categories/<slug:category_slug>/", views.CategoriesView.as_view(), name="categories"),
    path("tags/<slug:tag_slug>", views.TagsPostsListView.as_view(), name="tags")
]
