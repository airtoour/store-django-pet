from django.db import models


class Files(models.Model):
    """Модель таблицы Files"""
    file = models.FileField(upload_to="uploads")