from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from base.models import Product
from django.contrib.auth.decorators import login_required


def add_cart(request, pk):
    product = get_object_or_404(Product, id=pk)

    try:
        cart_product = Cart.objects.get(
            user=request.user,
            product=product
        )

        cart_product.quantity += 1
        cart_product.total_price += product.price
        cart_product.save()

    except:
        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1,
            total_price=product.price
        )

    return redirect('cart')

@login_required(login_url='login_')
def cart(request):
    cart_product = Cart.objects.filter(user=request.user)
    TA = 0
    for i in cart_product:
        TA += i.total_price



    return render(request,'cart.html',{'cart_product': cart_product,'TA': TA})


def removee(request, pk):
    cart_product = get_object_or_404(Cart, id=pk)
    cart_product.delete()

    return redirect('cart')


def plus(request, pk):
        cart_product = get_object_or_404(Cart, id=pk)
        
        cart_product.quantity += 1
        cart_product.total_price += cart_product.product.price
        cart_product.save()
        return redirect('cart')
    


def minus(request, pk):
    cart_product = get_object_or_404(Cart, id=pk)

    if cart_product.quantity > 0:
        cart_product.quantity -= 1
        cart_product.total_price -= cart_product.product.price
        cart_product.save()
    else:
        cart_product.delete()

    return redirect('cart')