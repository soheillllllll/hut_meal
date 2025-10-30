from django.db import models

from hut_meal_brand.models import upload_image


# Create your models here.


class Degree(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درجه'
        verbose_name_plural = 'درجه ها'


class ST(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, verbose_name="تصویر")

class Skill(ST):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'


class Team(ST):
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True, verbose_name='مهارت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تیم'
        verbose_name_plural = 'تیم ها '

    def get_team_detail_url(self):
        return f"/team-detail/{self.id}/{self.title.replace(' ', '-')}"
