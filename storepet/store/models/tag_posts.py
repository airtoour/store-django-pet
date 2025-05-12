from django.db import models
from django.urls import reverse


class TagPosts(models.Model):
    """Модель таблицы TagPosts"""

    tag = models.CharField(max_length=100, db_index=True, verbose_name="Тэг")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")

    objects = models.Manager()

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

        ordering = ("tag",)
        indexes = [
            models.Index(fields=("tag",), name="idx_tag_posts_tag"),
            models.Index(fields=("slug",), name="idx_tag_posts_unq_slug")
        ]

    def get_absolute_url(self):
        return reverse("tags", kwargs={"tag_slug": self.slug})

    def __str__(self):
        return self.tag
