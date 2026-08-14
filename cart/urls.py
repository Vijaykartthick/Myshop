from django.urls import path
from .views import *

urlpatterns = [
    path('cart/<int:pk>/', add_cart, name='add_cart'),
    path('carts/', cart, name='cart'),
    
    path('plus/<int:pk>/', plus, name='plus'),
    path('minus/<int:pk>/', minus, name='minus'),
    path('remove/<int:pk>/', removee, name='removee'),
]