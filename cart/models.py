from django.db import models
from django.contrib.auth.models import User
from base.models import Product
from orders.models import address




class Cart(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models. PositiveIntegerField(default=1)
    total_price = models. IntegerField()
    created_at= models. DateTimeField(auto_now_add=True)

class place_order(models.Model):
    STATUS_CHOICE = {
        'Pending':'Pending',
        'Confirmed':'Confirmed',
        'Shipped':'Shipped',
        'Delivered':'Delivered',
        'Cancelled':'Cancelled'
    }
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    addresss = models.ForeignKey(address,on_delete=models.SET_NULL,null=True,blank=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default='pending')
    create_at = models.DateTimeField(auto_now_add=True)

class orderItem(models.Model):
    order =  models.ForeignKey(place_order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
    def subtotal(self):
        return self.price*self.quantity

    