from django.shortcuts import render

from hut_meal_about.models import AboutUs


# Create your views here.



def about_us(request):
    about = AboutUs.objects.first()
    context = {'about': about}
    return render(request,'about-us.html', context)
