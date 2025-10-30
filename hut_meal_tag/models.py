from django.db import models

from hut_meal_blog.models import Blog
from hut_meal_product.models import Product


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    time = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات ')
    blogs = models.ManyToManyField(Blog, blank=True, verbose_name='بلاگ ها ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برچسب / تگ'
        verbose_name_plural = 'برچسب ها / تگ ها'
