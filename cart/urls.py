from django.urls import path
from .views import *

urlpatterns = [
    path('cart/<int:pk>/', add_cart, name='add_cart'),
    path('carts/', cart, name='cart'),
    
    path('plus/<int:pk>/', plus, name='plus'),
    path('minus/<int:pk>/', minus, name='minus'),
    path('remove/<int:pk>/', removee, name='removee'),

    path('checkout/',checkout,name='checkout'),
    path('placeorder/',placeorder,name='placeorder'),
    path('ordersuccess/<int:pk>',order_succfrully,name='order_succfully'),
    path('viewdetails/',viewdetails,name='viewdetails'),
    path('continew/',continew,name='continew'),
    path('order/',order,name='order'),
    path('delete/<int:pk>',delete,name='delete')
]