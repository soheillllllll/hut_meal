from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from hut_meal_category.models import BlogCategory, ProductCategory


# Create your views here.






def list_blog_categories(request):
    categories = BlogCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'list_category.html', context)


def list_product_categories(request):
    categories = ProductCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'list_product_category.html', context)
