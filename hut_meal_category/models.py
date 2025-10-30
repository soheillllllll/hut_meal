from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    name = models.CharField(max_length=100, verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی های محصولات '

    def __str__(self):
        return self.title


class BlogCategory(ProductCategory):

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی های بلاگ '

    def __str__(self):
        return self.title

