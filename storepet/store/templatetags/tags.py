from django import template
from django.db.models import Count

from store.models import Categories, TagPosts

register = template.Library()


@register.inclusion_tag("categories.html")
def show_categories(selected: int = 0):
    categories = Categories.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {"categories": categories, "selected": selected}


@register.inclusion_tag("tags.html")
def show_all_tags():
    return {"tags": TagPosts.objects.annotate(total=Count("tags")).filter(total__gt=0)}
