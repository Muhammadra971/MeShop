from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Order,OrderedItem
from Customers.models import Customer
from Product.models import Product

# Create your views here.

def ordered_list(request):
    if request.POST:
        user = request.user
        Custome = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        productid = request.POST.get('product_id')
        cart_obj,created = Order.objects.get_or_create(
            owner = Custome,
            order_status = Order.CART_STAGE,
        )
        product = Product.objects.get(pk = productid)
        Ordered_Item, created = OrderedItem.objects.get_or_create(
            product = product,
            owner = cart_obj,
            quantity = quantity
        )
        '''if created :
            Ordered_Item.quantity = quantity
            Ordered_Item.save()
        else:
            Ordered_Item.quantity = Ordered_Item.quantity+ quantity
            Ordered_Item.save()'''
    return redirect('cart')

def checkout(request):
    return render(request, 'checkout.html')