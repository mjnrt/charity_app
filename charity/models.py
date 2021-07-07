from django.db import models
from django.contrib.auth.models import User


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


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ManyToManyField(Institution)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=20)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    pickup_comment = models.TextField(max_length=240)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
