from django.shortcuts import render
from . models import Product
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def product_list(request):
    product = Product.objects.all()
    context = {
        'products': product,
    }
    return render(request, 'Products.html', context)

def product_detail(request):
    return render(request, 'detail.html')