from django import template
import store.views as views


register = template.Library()


@register.simple_tag()
def categories():
    return views.categories_db


@register.inclusion_tag('categories.html')
def inclusion_categories(selected: int = 0):
    return {"categories": views.categories_db, "selected": selected}
