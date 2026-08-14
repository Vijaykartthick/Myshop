from django.db import models

# Create your models here.
class Category(models.Model):
        cname = models.CharField(max_length=100,unique=True)
        cimage = models.ImageField(upload_to='categories/',blank=True,null=True)
        is_delete = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        
class Product(models.Model):
        category = models.ForeignKey(Category,on_delete=models.CASCADE)
        pname = models.CharField(max_length=200)
        pdescription = models.TextField()
        price = models.DecimalField(max_digits=10,decimal_places=2)
        stock = models.PositiveIntegerField(default=0)
        is_available = models.BooleanField(default=True)
        pimage = models.ImageField(upload_to='products/',default='Default.jpg')
        is_delete = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)  