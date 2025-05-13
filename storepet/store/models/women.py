from django.db import models
from django.urls import reverse

from .husbands import Husbands
from .tag_posts import TagPosts
from .categories import Categories


class PublishedManager(models.Manager):
    """Менеджер фильтрации опубликованных статей"""
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    """Модель таблицы Women"""

    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=256, db_index=True, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Описание")
    time_created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата создания")
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT,
        verbose_name="Статус"
    )

    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")

    # Cвязи
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name="posts", verbose_name="Категории")
    tags = models.ManyToManyField(TagPosts, blank=True, related_name="tags", verbose_name="Тэги")
    husband = models.OneToOneField(
        Husbands,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wife",
        verbose_name="Муж"
    )

    # todo кул практика вместо обычного поля
    # photos = models.ForeignKey(Files, on_delete=models.PROTECT, related_name="files", verbose_name="Фото")

    class Meta:
        verbose_name = "Известная женщина"
        verbose_name_plural = "Известные женщины"

        ordering = ("title",)
        indexes = [
            models.Index(fields=("title",), name="idx_women_title"),
            models.Index(fields=("time_created",), name="idx_women_time_created"),
            models.Index(fields=("slug",), name="idx_women_unq_slug")
        ]

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname="posts", kwargs={"post_slug": self.slug})
