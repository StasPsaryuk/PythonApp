from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"id": self.id})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"id": self.id})

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
