from django.urls import path

from .views import ProductListByBrand

app_name = "hut_meal_brand"

urlpatterns = [
    path('products/brands/<brand_name>', ProductListByBrand.as_view(), name='product_list_by_brand'),
]
