from django.urls import path
from . import views
urlpatterns = [
    path('cart/', views.ordered_list, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
