from django import template
from store.models import Categories, TagPosts

register = template.Library()


@register.inclusion_tag("categories.html")
def show_categories(selected: int = 0):
    return {"categories": Categories.objects.all(), "selected": selected}


@register.inclusion_tag("tags.html")
def show_all_tags():
    return {"tags": TagPosts.objects.all()}
