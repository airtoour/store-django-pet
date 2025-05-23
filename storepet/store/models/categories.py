from django.db import models
from django.urls import reverse


class Categories(models.Model):
    """Модель таблицы Categories (Категории)"""

    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")

    objects = models.Manager()

    class Meta:
        verbose_name = "Категория женщин"
        verbose_name_plural = "Категории женщин"

        indexes = [
            models.Index(fields=("name",), name="idx_categories_unq_tag"),
            models.Index(fields=("slug",), name="idx_categories_unq_slug")
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(viewname="categories", kwargs={"category_slug": self.slug})
