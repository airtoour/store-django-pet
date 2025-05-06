from django import template
from store.models import Categories


register = template.Library()

CATS = Categories.objects.all()

@register.simple_tag()
def categories():
    return CATS


@register.inclusion_tag('categories.html')
def inclusion_categories(selected: int = 0):
    return {"categories": CATS, "selected": selected}
