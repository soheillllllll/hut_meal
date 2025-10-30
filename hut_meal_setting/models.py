from django.db import models
from hut_meal_Team.models import ST
from hut_meal_brand.models import upload_image


# Create your models here.


class FeaturesRestaurant(ST):
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'ویژگی رستوران'
        verbose_name_plural = 'ویژگی های رستوران'


class Slider(ST):
    name = models.CharField(max_length=35)
    skills = models.CharField(max_length=29)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'اسلایدر1'
        verbose_name_plural = 'اسلایدرها 1'


class SliderBlog(ST):
    link = models.CharField(max_length=100, verbose_name='عنوان در url')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'اسلایدر بلاگ'
        verbose_name_plural = 'اسلایدر های بلاگ'


class HomePageSettings(ST):
    logo= models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name="تصویر لوگو")
    title_image = models.CharField(max_length=30, verbose_name='title_image')
    description_image = models.CharField(max_length=40, verbose_name='description_image')
    footer_text = models.CharField(max_length=300, verbose_name='footer_text ')
    address = models.CharField(max_length=130, verbose_name='address')
    phone = models.CharField(max_length=20, verbose_name='phone')
    email = models.CharField(max_length=40, verbose_name='email')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'تنظیمات صفحه اول '
        verbose_name_plural = 'تنظیمات صفحه اول'

class MainSlider(ST):
    title2 = models.CharField(max_length=60, verbose_name='title2')
    title3 = models.CharField(max_length=100, verbose_name='title3')
    discount = models.IntegerField(verbose_name='discount')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'اسلایدر اصلی'
        verbose_name_plural = 'اسلایدر اصلی'

