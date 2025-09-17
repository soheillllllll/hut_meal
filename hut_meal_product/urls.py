from django.urls import path

from .views import ProductListView, product_detail, ProductListView2

app_name = 'hut_meal_contact'

urlpatterns = [
    path('products', ProductListView.as_view(), name='products_list1'),
    path('products-list', ProductListView2.as_view(), name='products_list2'),
    path('products/<int:product_id>/<title>/', product_detail, name='product_detail'),
]