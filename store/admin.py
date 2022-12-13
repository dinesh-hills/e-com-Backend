from django.contrib import admin
from .models import Product, Customer, Order

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory', 'collection']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_select_related = ['user']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at']