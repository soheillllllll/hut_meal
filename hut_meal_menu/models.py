from django.db import models

from hut_meal_category.models import ProductCategory


# Create your models here.
class Meals(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'وعده'
        verbose_name_plural = 'وعده ها'


class Menu(models.Model):
    title = models.CharField(max_length=110)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="قیمت")
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی')
    meals = models.ManyToManyField(Meals, blank=True, verbose_name='انتخاب وعده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'منو'
        verbose_name_plural = 'منو ها'





