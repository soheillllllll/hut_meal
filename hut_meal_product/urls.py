from django.urls import path

from .views import ProductListView, product_detail, ProductListView2, SearchProducts

app_name = 'hut_meal_product'

urlpatterns = [
    path('products-list1', ProductListView.as_view(), name='products_list1'),
    path('products-list2', ProductListView2.as_view(), name='products_list2'),
    path('products/<int:product_id>/<title>/', product_detail, name='product_detail'),
    path('products/search/', SearchProducts.as_view(), name='product_search'),
]