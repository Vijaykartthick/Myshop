from django.urls import path
from .views import *

urlpatterns =[
    path('address/',add_address,name='add_address'),
    path('address_list',address_list,name='address_list'),

    path('update_address/<int:pk>',update_address,name='update_address'),
    path('delete_address/<int:pk>',delete_address,name='delete_address')
    
]