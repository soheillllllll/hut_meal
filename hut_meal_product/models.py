import os
import random

from django.db import models
from django.db.models import Q

# from store_brand.models import ProductBrand
# from store_products_category.models import ProductCategory


# Create your models here.


def get_file_extension(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image(instance, filename):
    rand_name = random.randint(1, 999999999999999)
    name, ext = get_file_extension(filename)
    file_name = f"{instance.id}-{rand_name}{ext}"
    return f"products/{file_name}"

def upload_image_gallery(instance, filename):
    rand_name = random.randint(1, 999999999999999)
    name, ext = get_file_extension(filename)
    file_name = f"{instance.id}-{rand_name}{ext}"
    return f"gallery/{file_name}"


class ProductDiscount(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان تخفیف')
    percentage = models.IntegerField( verbose_name='درصد تخفیف %')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تخیف'
        verbose_name_plural = 'تخفیف ها'

class ProductSize(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان سایز')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز ها'


class ProductColor(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان رنگ')
    image_code = models.CharField(max_length=100, verbose_name='کد رنگ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


class ProductManager(models.Manager):
    def get_product_by_id(self, productid):
        qs = self.get_queryset().filter(id=productid, active=True)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_active_product(self):
        return self.get_queryset().filter(active=True)


    def search_products(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
        return self.get_queryset().filter(lookup, active=True).distinct()

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_product_by_brand(self, brand_name):
        return self.get_queryset().filter(brand__name__iexact=brand_name, active=True)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    #    slug = models.SlugField(blank=True, unique=True)
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="قیمت")
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name="تصویر")
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    time = models.DateTimeField(auto_now_add=True)
    # categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی')
    color = models.ManyToManyField(ProductColor, blank=True, verbose_name='رنگ')
    size = models.ManyToManyField(ProductSize, blank=True, verbose_name='سایز')
    # brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند')
    featured = models.BooleanField(default=False, verbose_name='محصول ویژه')
    visits = models.IntegerField(default=0, verbose_name='تعداد مشاهده')
    discount = models.ForeignKey(ProductDiscount, on_delete=models.CASCADE, verbose_name='درصد تخفیف %')

    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_product_detail_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"

    def price2(self):
        price2 = (self.price) - (self.price) * (self.discount.percentage) / 100
        return price2





class ProductGallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_image_gallery, null=True, blank=True, verbose_name="تصویر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='انتخاب محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural='گالری تصاویر'

    def __str__(self):
        return self.title