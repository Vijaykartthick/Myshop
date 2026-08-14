from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q


@login_required(login_url='login_')
def home(request):

    q = request.GET.get('q', '')
    cat = request.GET.get('cat', '')

    if q:
        all_data = Product.objects.filter(Q(pname__icontains=q) |
            Q(pdescription__icontains=q),
            is_available=True
        )

    elif cat:
        all_data = Product.objects.filter(category__cname=cat,is_available=True)

    else:
        all_data = Product.objects.filter(is_available=True)

    return render(request, "home.html", {"all_data": all_data,"q": q,"cat": cat})

def details(request,pk):
    product = get_object_or_404(Product,id = pk)
    category_product = Product.objects.filter(category=product.category) 
    return render(request,'view.html',{'product' :product ,
                                       'category':category_product
                                       })