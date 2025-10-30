from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.shortcuts import render, redirect

from hut_meal_comment.forms import CommentProductForm
from hut_meal_comment.models import CommentProduct
from hut_meal_product.models import Product, ProductGallery, ProductSize, ProductColor


# Create your views here.





class ProductListView(ListView):
    template_name = 'product_list1.html'
    paginate_by = 4
    def get_queryset(self):
        return Product.objects.get_active_product()


class ProductListView2(ProductListView):
    template_name = 'product_list2.html'
    paginate_by = 6


def product_detail(request, *args, **kwargs):
    get_product_id = kwargs['product_id']
    # new_order_form = UserNewOrderForm(request.POST or None, initial=({'product_id': get_product_id}))
    # tag_form = TagForm(request.POST or None)
    product = Product.objects.get_product_by_id(get_product_id)
    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()[:3]
    comment_form = CommentProductForm(request.POST or None)
    comments = product.comment_products.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentProductForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
            return HttpResponseRedirect(request.path_info)

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
        'comments': comments,
        'comment_form': comment_form,
        'related_products': related_products,
        # 'tag': tag,
        # 'tag_form': tag_form,
        # 'new_order_form':new_order_form
    }
    return render(request, 'product_detail.html', context)


class SearchProducts(ListView):
    template_name = 'product_list2.html'
    paginate_by = 10
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Product.objects.search_products(query)
        return Product.objects.get_active_product()


def special_products(request):
    products = Product.objects.filter(featured=True)[:4]
    context= {'products': products}
    return render(request,'speial_products.html', context)