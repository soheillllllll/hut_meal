from lib2to3.fixes.fix_input import context

from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView

from hut_meal_brand.models import ProductBrand
from hut_meal_product.models import Product


# Create your views here.


class ProductListByBrand(ListView):
    template_name = 'product_list2.html'

    paginate_by = 8

    def get_queryset(self):
        brand_name = self.kwargs['brand_name']
        brands = ProductBrand.objects.filter(name__iexact=brand_name)
        if brands is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Product.objects.get_product_by_brand(brand_name)


def render_brand_list(request):
    brands = ProductBrand.objects.all()
    context={'brands':brands}
    return render(request, 'render_brand_list.html', context)