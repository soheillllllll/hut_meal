"""
URL configuration for hut_meal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from hut_meal import settings
from hut_meal.views import home_page, header, footer
from hut_meal_about.views import about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
    path('', include('hut_meal_product.urls', namespace='product')),
    path('', include('hut_meal_profile.urls', namespace='profile')),
    path('', include('hut_meal_order.urls', namespace='order')),
    path('about-us', about_us, name='about_us'),

    path('', include('hut_meal_contact.urls', namespace='contact')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
