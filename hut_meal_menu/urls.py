from django.urls import path

from hut_meal_menu.views import menu_page

app_name = "hut_meal_menu"

urlpatterns = [
    path('menu_page', menu_page, name='menu_page'),
]
