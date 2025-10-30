from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from hut_meal_product.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    paid = models.BooleanField(default=False, verbose_name='پراداخت شده/نشده')
    status = models.CharField(default='pending')
    pay_data = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=15, decimal_places=0, verbose_name="قیمت")


    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return self.user.get_full_name()

    def total_price2(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.product.price2() * detail.count

        return amount

    def total_count(self):
        co = 0
        for detail in self.orderdetail_set.all():
            co += 1
        return co




class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='i')
    price = models.IntegerField()

    class Meta:
        verbose_name = 'جزئیات سیدخرید'
        verbose_name_plural = 'جزئیات های سبد خرید'

    def __str__(self):
        return self.product.title

    def product_sum_in_cart(self):
        return self.product.price2() * self.count


class Payments(models.Model):
    ref_id = models.CharField(max_length=400)
    card_pan = models.CharField(max_length=400)
    amount = models.CharField(max_length=400)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.ref_id
