from django.db import models

# Create your models here.

import os
import random

def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image(instance, filename):
    rand_name = random.randint(1, 999999999999999)
    name, ext = get_file_extension(filename)
    file_name = f"{instance.id}-{rand_name}{ext}"
    return f"brands/{file_name}"

class ProductBrand(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    name = models.CharField(max_length=100, verbose_name='عنوان در url')
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name="تصویر")

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند های محصولات'

    def __str__(self):
        return self.title