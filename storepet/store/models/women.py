from django.db import models
from django.urls import reverse

from .husbands import Husbands
from .tag_posts import TagPosts
from .categories import Categories


class Women(models.Model):
    """Модель таблицы Women"""

    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=256, db_index=True)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True, db_index=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)

    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    # Cвязи
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField(TagPosts, blank=True, related_name="tags")
    husband = models.OneToOneField(Husbands, on_delete=models.SET_NULL, null=True, blank=True, related_name="wife")

    class Meta:
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
