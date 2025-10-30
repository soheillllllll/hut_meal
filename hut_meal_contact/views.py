from django.contrib import messages
from django.shortcuts import render

from hut_meal_contact.forms import ContactUsForm
from hut_meal_contact.models import Contact
from hut_meal_setting.models import HomePageSettings


# Create your views here.



def contact_us(request):
    setting = HomePageSettings.objects.first()
    contact_form = ContactUsForm(data=request.POST or None)
    if contact_form.is_valid():
        contact_form.save()
        messages.info(request, 'Your message was sent successfully.')
    context = {'setting': setting}
    return render(request, 'contact-us.html', context)