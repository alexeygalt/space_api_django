from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username


class Indication(models.Model):
    """model to indication object"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    axis = models.CharField(max_length=100, null=False)
    distance = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Инструкция"
        verbose_name_plural = "Инструкции"


