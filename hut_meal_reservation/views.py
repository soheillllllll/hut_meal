from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

from hut_meal_order.views import send_request
from hut_meal_reservation.forms import ReservationForm
from hut_meal_reservation.models import Reservation, Table


# Create your views here.

def reservation(request):
    reservation_form = ReservationForm(request.POST or None)
    if reservation_form.is_valid():
        name = reservation_form.cleaned_data.get('name')
        email = reservation_form.cleaned_data.get('email')
        reservation_id = request.POST.get('table')
        reservation_item = Reservation.objects.filter(id=reservation_id).first()
        reservation_item.Customer_email = email
        reservation_item.customer_name = name
        reservation_item.save()
        return redirect(reverse('order:request', kwargs={'id': reservation_id, 'letter': 'a'}))


    context ={}
    return redirect("/cart")






def ajax_handler(request,id):
# index.js  <<-----
    print(1)
    id = str(id)
    # print(time)
    reservation = Reservation.objects.filter(time_id=id, active=False).values_list('id','table__title')
    print(reservation)
    reservation = dict(reservation)
    return JsonResponse({
        'reservation' : reservation,
    })
