from django.contrib import admin, messages
from django.db.models import QuerySet
from django.http import HttpRequest

from ..models import Women


class MarriedFilter(admin.SimpleListFilter):
    """Фильтр для панели Women"""

    title = "Статус женщин"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [("married", "Замужем"), ("single", "Не замужем")]

    def queryset(self, request, queryset):
        if self.value() == "married":
            return queryset.filter(husband__isnull=False)
        return queryset.filter(husband__isnull=True)


class WomenAdmin(admin.ModelAdmin):
    """Панель для администрирования таблицы Women"""

    exclude = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)

    list_display = ("title", "time_created", "is_published", "category", "brief_info")
    list_display_links = ("title",)
    list_editable = ("is_published",)
    list_filter = (MarriedFilter, "category__name", "is_published")

    list_per_page = 10

    ordering = ("time_created", "id")

    actions = ("set_published", "set_draft")

    search_fields = ("title", "category__name")

    @admin.display(description="Краткое описание", ordering="content")
    def brief_info(self, women: Women) -> str:
        """Метод, добавляющий поле в панель"""
        return f"Описание {len(women.content)} символов"

    @admin.action(description="Опубликовать записи")
    def set_published(self, request: HttpRequest, queryset: QuerySet) -> None:
        """Метод, позволяющий опубликовывать статьи"""
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, message=f"Опубликовано {count} записей")

    @admin.action(description="Снять с публикации")
    def set_draft(self, request: HttpRequest, queryset: QuerySet) -> None:
        """Метод, позволяющий снимать с публикации статьи"""
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации", messages.WARNING)
