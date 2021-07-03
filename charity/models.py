from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    TYPE_CHOICES = (
        ("fundacja", "fundacja"),
        ("organizacja pozarządowa", "organizacja pozarządowa"),
        ("zbiórka lokalna", "zbiórka lokalna")
    )
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    type = models.CharField(max_length=64, choices=TYPE_CHOICES, default="fundacja")
    categories = models.ManyToManyField(Category)
