from django.shortcuts import render

from hut_meal_blog.models import Blog
from hut_meal_brand.models import ProductBrand
from hut_meal_order.models import Order
from hut_meal_reservation.forms import ReservationForm
from hut_meal_reservation.models import Time, Reservation
from hut_meal_setting.models import FeaturesRestaurant, Slider, SliderBlog, HomePageSettings, MainSlider


def header(request):
    setting = HomePageSettings.objects.first()
    if request.user.is_authenticated:
        context = {
            'order': None,
            'setting': setting
        }
        open_order = Order.objects.filter(user_id=request.user.id, status="pending").first()
        if open_order is None:
            open_order = Order.objects.create(user_id=request.user.id, paid=False)

        if open_order is not None:
            context['total_count'] = open_order.total_count()

    else:
        context = {
            'setting': setting
        }
    return render(request, 'base/header.html', context)


def footer(request):
    latest_blogs = Blog.objects.order_by('-id')[:3]
    setting = HomePageSettings.objects.first()
    context = {
        'latest_blogs': latest_blogs,
        'setting': setting
    }
    return render(request, 'base/footer.html', context)


import json


def home_page(request):
    reservation_form = ReservationForm(request.POST or None)
    time_reservation = Time.objects.all()
    features_restaurant = FeaturesRestaurant.objects.all()
    slider1 = Slider.objects.all()
    slider_blog = SliderBlog.objects.all()
    setting = HomePageSettings.objects.first()
    main_slider = MainSlider.objects.all()
    price_table = 20
    context = {
        'main_slider': main_slider,
        'setting': setting,
        'reservation_form': reservation_form,
        'time_reservation': time_reservation,
        'features_restaurant': features_restaurant,
        'slider1': slider1,
        'slider_blog': slider_blog,
        'price_table': price_table,
    }
    return render(request, 'index.html', context)
