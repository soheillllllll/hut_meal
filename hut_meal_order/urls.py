from django.urls import path

from .views import cart_page

app_name = 'hut_meal_order'

urlpatterns = [
    path('cart-page', cart_page, name='cart_page')
]