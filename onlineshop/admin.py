from django.contrib import admin

from .models import Category, Product, order

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','category_description', 'created_at', 'updated_at']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_description', 'price', 'image', 'category', 'created_at', 'updated_at']



@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_email', 'product','customer_address','quantity','created_at', 'updated_at']