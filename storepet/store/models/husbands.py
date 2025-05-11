from django.db import models
from django.urls import reverse


class Husbands(models.Model):
    """Модель таблицы Husband (мужья)"""

    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    objects = models.Manager()

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("husbands", kwargs={...})

    def __str__(self):
        return self.name
