from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def product_list(request):
    return render(request, 'Products.html')

def product_detail(request):
    return render(request, 'detail.html')