from django.db import models
# from django.urls import reverse


class Husbands(models.Model):
    """Модель таблицы Husband (мужья)"""

    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(null=True, verbose_name="Возраст")
    m_count = models.IntegerField(blank=True, default=0, verbose_name="Количество женитьб")

    objects = models.Manager()

    class Meta:
        verbose_name = "Муж известной женщины"
        verbose_name_plural = "Мужья известных женщин"

        ordering = ("name",)

    def __str__(self):
        return self.name
