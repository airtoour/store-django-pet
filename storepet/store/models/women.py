from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from .husbands import Husbands
from .tag_posts import TagPosts
from .categories import Categories


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
        verbose_name="Статус публикации"
    )

    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname="posts", kwargs={"post_slug": self.slug})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)