from django.contrib import admin
from ..models import (
    Women,
    Categories,
    TagPosts,
    Husbands
)
from .women import WomenAdmin
from .categories import CategoriesAdmin

admin.site.register(Women, WomenAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(TagPosts)
admin.site.register(Husbands)
