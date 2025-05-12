from django.contrib import admin


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("name",)

    list_per_page = 10

    ordering = ("id",)