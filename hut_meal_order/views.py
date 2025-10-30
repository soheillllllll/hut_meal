from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from django.urls import reverse
from hut_meal_order.forms import UserNewOrderForm
from hut_meal_order.models import Order, Payments
from hut_meal_product.models import Product
from hut_meal_reservation.forms import ReservationForm
from hut_meal_reservation.models import Reservation, Table



# Create your views here.


@login_required(login_url='/login')
def cart_page(request):
    print('total')
    context = {
        'order': None,
        'details': None,
        'total_price2': 0
    }
    open_order = Order.objects.filter(user_id=request.user.id, status='pending').first()
    print(open_order)
    if open_order is None:
        open_order = Order.objects.create(user_id=request.user.id, paid=False)

    print(open_order)
    order_detail = open_order.orderdetail_set.filter(order_id=open_order.id)

    if open_order is not None:
        context['order'] = open_order
        context['details'] = order_detail
        context['total_price2'] = open_order.total_price2()

    return render(request, 'cart.html', context)


@login_required(login_url='/login')
def add_new_item_order(request, *args, **kwargs):
    count = 1
    print(count)
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        count = new_order_form.cleaned_data.get('count')
    print(count)
    product_id = kwargs['product_id']
    order = Order.objects.filter(user_id=request.user.id, status="pending").first()
    if order is None:
        order = Order.objects.create(user_id=request.user.id, paid=False)

    product = Product.objects.get_product_by_id(product_id)

    order_detail = order.orderdetail_set.filter(product_id=product_id).first()
    if order_detail is None:
        count = count
        order.orderdetail_set.create(product_id=product.id, count=count, price=product.price2())
        order.price = order.total_price2()
        order.save()

    else:
        order_detail.count += count
        order_detail.save()
        order.price = order.total_price2()
        order.save()

    return redirect('/cart-page')


@login_required(login_url='/login')
def remove_cart_item(request, *args, **kwargs):
    product_id = kwargs['product_id']
    order = Order.objects.filter(user_id=request.user.id, status="pending").first()
    order_detail = order.orderdetail_set.filter(product_id=product_id).first()
    if order_detail.count > 1:
        order_detail.count -= 1
        order_detail.save()
        order.price = order.total_price2()
        order.save()
    else:
        order_detail.delete()
        order.price = order.total_price2()
        order.save()
    return redirect('/cart-page')


# zarinpal import file
from django.conf import settings
import requests
import json
from django.http import HttpResponse

# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

from django.http import HttpResponse, Http404
from django.shortcuts import redirect
import requests
import json
import time
from django.core.serializers.json import DjangoJSONEncoder

ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify'


def send_request(request, *args, **kwargs):
    id = kwargs['id']
    letter = kwargs['letter']
    req_data = {
        "merchant_id": settings.MERCHANT,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }

    if letter == "a":
        reservation = Reservation.objects.filter(id=id).first()
        if reservation is not None:
            req_data["amount"] = reservation.table.price
            req_data["callback_url"] = f"{CallbackURL}/{id}/a"
    else:
        open_order: Order = Order.objects.filter(id=id).first()
        if open_order is not None:
            total_price2 = open_order.total_price2()
            print(total_price2)
            req_data["amount"] = total_price2
            req_data["callback_url"] = f"{CallbackURL}/{id}/b"
        # req_data = {
        #     "merchant_id": settings.MERCHANT,
        #     "amount": total_price2,
        #     "callback_url": f"{CallbackURL}/{open_order.id}",
        #     "description": description,
        #     "metadata": {"mobile": mobile, "email": email}
        # }
    req_header = {"accept": "application/json", "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data, cls=DjangoJSONEncoder), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request, *args, **kwargs):
    id = kwargs['id']
    letter = kwargs['letter']
    if letter == "a":
        reservation = Reservation.objects.filter(id=id).first()
        total_price2 = reservation.table.price

    else:
        open_order: Order = Order.objects.filter(user_id=request.user.id, id=id).first()
        total_price2 = open_order.total_price2()
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']


    if request.GET.get('Status') == 'OK':
        print(1)
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": settings.MERCHANT,
            "amount": total_price2,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data, cls=DjangoJSONEncoder), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                card_pan = req.json()['data']['card_pan']
                ref_id = req.json()['data']['ref_id']

                if letter == "a":
                    reservation.active = True
                    reservation.save()
                else:
                    print('@3')

                    order = Order.objects.get_queryset().get(id=id)
                    payment = Payments.objects.create(order_id=id)

                    payment.ref_id = ref_id
                    payment.card_pan = card_pan
                    order.paid = True
                    order.status = 'paid'
                    order.pat_date = time.time()
                    order.pay_data = datetime.now()
                    payment.save()
                    order.save()
                context = {
                    'refID': str(req.json()['data']['ref_id'])
                }
                messages.info(request, 'Payment was successful.')
                # return render(request, 'my-orders.html', context)
                # return redirect(reverse('orders:order_details', kwargs={'order_id': order_id}))
                return redirect('/')

            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
