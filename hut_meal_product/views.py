from django.http import Http404
from django.views.generic.list import ListView
from django.shortcuts import render
from hut_meal_product.models import Product, ProductGallery, ProductSize, ProductColor


# Create your views here.





class ProductListView(ListView):
    template_name = 'product_list.html'
    paginate_by = 8
    def get_queryset(self):
        return Product.objects.get_active_product()


class ProductListView2(ListView):
    template_name = 'product_list2.html'
    paginate_by = 8
    def get_queryset(self):
        return Product.objects.get_active_product()


def product_detail(request, *args, **kwargs):
    get_product_id = kwargs['product_id']
    # new_order_form = UserNewOrderForm(request.POST or None, initial=({'product_id': get_product_id}))
    # tag_form = TagForm(request.POST or None)
    product = Product.objects.get_product_by_id(get_product_id)
    # related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()[:4]

    if product is None:
        raise Http404('محصول مورد نظر یافت نشد!')
    product.visits += 1
    product.save()

    gallery = ProductGallery.objects.filter(product_id=get_product_id)
    size = ProductSize.objects.filter(product=product)
    color = ProductColor.objects.filter(product=product)

    # tag = product.tag_set.all()

    context = {
        'product': product,
        'gallery': gallery,
        'size': size,
        'color': color,
        # 'related_products': related_products,
        # 'tag': tag,
        # 'tag_form': tag_form,
        # 'new_order_form':new_order_form
    }
    return render(request, 'product_detail.html', context)