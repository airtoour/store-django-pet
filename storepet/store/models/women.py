from django.db import models
from django.urls import reverse


class Women(models.Model):
    """Модель таблицы Women"""

    title = models.CharField(max_length=256)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        ordering = ("-title",)
        indexes = [
            models.Index(fields=("time_created",), name="idx_women_time_created"),
            models.Index(fields=("title",), name="idx_women_title")
        ]

    def get_absolute_url(self):
        return reverse(viewname="post", kwargs={"post_slug": self.slug})