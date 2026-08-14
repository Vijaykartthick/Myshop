from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('details/<int:pk>',details,name='details')
   
]