from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from base.models import Product
from orders.models import address
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import place_order,orderItem
from django.contrib.auth.models import User


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

def checkout(request):
    addresses = address.objects.filter(user = request.user)
    cart_item = Cart.objects.filter(user = request.user)


    # TA=0
    # for i in cart:
    #     TA+=i.total_price 

    grant_total = sum(i.total_price for i in cart_item)
    context = {
        'cart_item':cart_item,
        'addresses':addresses,
        'grant_total':grant_total
    }
        


    return render(request,'checkout.html',context)

@login_required(login_url='login_')
def placeorder(request):
    if request.method == "POST":

        address_id = request.POST.get('address')

        if not address_id:
            return redirect('checkout')

        addresses = get_object_or_404(
            address,
            id=address_id,
            user=request.user
        )

        cart_products = Cart.objects.filter(user=request.user)

        if not cart_products.exists():
            return redirect('cart')

        grant_price = sum(i.total_price for i in cart_products)

        order = place_order.objects.create(
            user=request.user,
            addresss=addresses,
            total_amount=grant_price
        )

        for i in cart_products:
            orderItem.objects.create(
                order=order,
                product=i.product,
                price=i.product.price,
                quantity=i.quantity
            )

        return redirect('order_succfully', order.id)

    return redirect('checkout')

@login_required(login_url='login_')
def order_succfrully(request, pk):
    order_products = get_object_or_404(place_order,id=pk,user=request.user)
    products = order_products.items.all()
    return render(request,'order_succfully.html',{'orders': order_products,'products': products}
    )

def viewdetails(request):
    return redirect('order')

def continew(request):
    return redirect('home')


def order(request):
    products = place_order.objects.filter(user=request.user).order_by('-create_at')
    return render(request,'order.html',{'products':products})

def delete(request,pk):
    deleteed = place_order.objects.get(id = pk)
    deleteed.delete()
    return redirect('order')