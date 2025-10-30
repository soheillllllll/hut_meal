from django.contrib import admin

from hut_meal_category.models import ProductCategory, BlogCategory

# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(BlogCategory)