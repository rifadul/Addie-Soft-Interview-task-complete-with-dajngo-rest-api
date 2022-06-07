from django.contrib import admin
from .models import Sales,Product,SalesDetails

# Register your models here.
@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['id','customerName', 'mobileNo','totalAmount']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','productName', 'ProductDetails','productPrice']

@admin.register(SalesDetails)
class SalesDetailsAdmin(admin.ModelAdmin):
    list_display=['id','salesId', 'productId','quantity','unitPrice','total']

