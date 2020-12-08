from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name_plural = 'Categories'


class Aliment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nutriscore = models.CharField(max_length=100)
    image_url = models.URLField(unique=True)
    product_url = models.URLField(unique=True)
    sugar = models.CharField(max_length=100, null=True, default=None)
    fat = models.CharField(max_length=100, null=True, default=None)
    salt = models.CharField(max_length=100, null=True, default=None)
    energy = models.CharField(max_length=100, null=True, default=None)

    category = models.ForeignKey(Category, related_name='aliments',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aliment = models.ForeignKey(Aliment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
