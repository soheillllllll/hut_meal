from django.urls import path

from .views import ajax_handler, reservation

app_name = 'hut_meal_reservation'

urlpatterns = [
    path('reservation/', reservation, name="reservation_page"),
    path('ajax_handler/<id>', ajax_handler, name="ajax_handler"),

]
