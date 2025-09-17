from django.contrib import admin

# Register your models here.
from .models import Product, ProductGallery, ProductColor, ProductSize, ProductDiscount


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active', 'featured']

    class Meta:
        Model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
admin.site.register(ProductColor)
admin.site.register(ProductSize)
admin.site.register(ProductDiscount)

