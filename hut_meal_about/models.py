from django.db import models

from hut_meal_brand.models import upload_image


# Create your models here.



class AboutUs(models.Model):
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name="تصویر")
    title_first = models.CharField(max_length=60)
    description_first = models.TextField()
    Persons_name= models.CharField(max_length=20)
    def __str__(self):
        return self.Persons_name
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
