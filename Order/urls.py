from django.urls import path
from . import views
urlpatterns = [
    path('order/', views.order_list, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
