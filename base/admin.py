from django.contrib import admin
from .models import Product,Category

# Register your models here.
@admin.register(Category)
class category(admin.ModelAdmin):
    model  = Category
    list_display = ['cname']

@admin.register(Product)
class productadmin(admin.ModelAdmin):
    model = Product
    list_display =['category','pname','price','stock','is_available']