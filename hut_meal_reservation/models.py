from django.db import models

from hut_meal_product.models import Product


# Create your models here.


class Time(models.Model):
    time_res = models.IntegerField()
    def __str__(self):
        return str(self.time_res)



class Table(models.Model):
    title = models.CharField(max_length=100)
    table_number = models.IntegerField()
    mnimum_seats = models.IntegerField()
    maximum_seats = models.IntegerField()
    time = Time.objects.all()
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="قیمت")

    def __str__(self):
        return str(self.title)




class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    customer_name= models.CharField(max_length=100)
    Customer_email= models.EmailField(max_length=70)
    def __str__(self):
        return str(self.table)

