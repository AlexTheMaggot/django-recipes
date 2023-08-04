from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="images/", default=None, verbose_name="Фото")
    ingredients = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    time_to_cook = models.DurationField(default=15)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)


