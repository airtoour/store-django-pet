from .methods import (
    index,
    show_post,
    show_categories,
    show_tag_posts_list,
    contact,
    login,
    about,
    page_not_found
)

from .pages import (
    add_page,
    PagesAddView,
    PagesAddFormView,
    PagesCreateView,
    PagesUpdateView,
    PagesDeleteView
)

from .models import (
    WomenHomeView,
    CategoriesView,
    ShowPostView,
    TagsPostsListView
)