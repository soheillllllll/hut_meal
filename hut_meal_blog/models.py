import os
import random

from django.db import models
from django.db.models import Q

from hut_meal_Team.models import ST
from hut_meal_category.models import BlogCategory


# Create your models here.


def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image(instance, filename):
    rand_name = random.randint(1, 999999999999999)
    name, ext = get_file_extension(filename)
    file_name = f"{instance.id}-{rand_name}{ext}"
    return f"blog/{file_name}"


class BlogManager(models.Manager):
    def get_blog_by_id(self, blog_id):
        qs = self.get_queryset().filter(id=blog_id, active=True)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_active_blog(self):
        return self.get_queryset().filter(active=True)

    def search_blogs(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query) | Q(categories__title__icontains=query)
        return self.get_queryset().filter(lookup, active=True).distinct()

    def get_blog_by_category(self, category_link):
        return self.get_queryset().filter(categories__link__iexact=category_link)


class Blog(ST):
    categories = models.ManyToManyField(BlogCategory, blank=True, verbose_name='دسته بندی')
    user = models.CharField(max_length=30)
    user_description = models.CharField(max_length=90)
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    visits = models.IntegerField(default=0, verbose_name='تعداد مشاهده')

    objects = BlogManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'

    def get_blog_detail_url(self):
        return f"/blog/{self.id}/{self.title.replace(' ', '-')}"
