from django.shortcuts import render

from hut_meal_menu.models import Menu


# Create your views here.



def menu_page(request):
    menus_lunch = Menu.objects.filter(meals__title__iexact='lunch')
    menus_dinner = Menu.objects.filter(meals__title__iexact='dinner')
    menus_breakfast = Menu.objects.filter(meals__title__iexact='breakfast')
    context = {
        'menus_lunch': menus_lunch,
        'menus_dinner': menus_dinner,
        'menus_breakfast': menus_breakfast,
    }
    return render(request, 'menu.html', context)

