from django.db import models
from django.urls import reverse


class TagPosts(models.Model):
    """Модель таблицы TagPosts"""

    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()

    class Meta:
        ordering = ("tag",)
        indexes = [
            models.Index(fields=("tag",), name="idx_tag_posts_tag"),
            models.Index(fields=("slug",), name="idx_tag_posts_unq_slug")
        ]

    def get_absolute_url(self):
        return reverse("tags", kwargs={"tag_slug": self.slug})

    def __str__(self):
        return self.tag
