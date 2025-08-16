from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:8]
    recent_products = Product.objects.order_by('-created_at')[:8]
    context = {
        'featured_products': featured_products,
        'recent_products': recent_products,
    }
    return render(request, 'index.html', context)
def product_list(request):
    page = 0
    if request.GET:
        page = int(request.GET.get('page',1))
    product_list = Product.objects.all()
    product_paginator = Paginator(product_list, 9)
    product_list = product_paginator.get_page(page)

    context = {
        'products': product_list,
    }
    return render(request, 'Products.html', context)

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context)