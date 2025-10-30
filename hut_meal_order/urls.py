from django.urls import path

from .views import cart_page, add_new_item_order, remove_cart_item, send_request, verify

app_name = 'hut_meal_order'

urlpatterns = [
    path('cart-page', cart_page, name='cart_page'),
    # path('account/order/', order, name='order'),
    # path('account/order/order-detail/<order_id>', order_detail, name='order_details'),
    path('add-naw-item-order/<product_id>', add_new_item_order, name='add_new_item_order'),
    path('remove-cart-item/<product_id>', remove_cart_item),
    path('request/<id>/<letter>', send_request, name='request'),
    path('verify/<id>/<letter>', verify, name='verify'),
]
