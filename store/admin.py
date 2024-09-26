from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'image', 'image2', 'image3')
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('email', 'phone')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity', 'price', 'date', 'address', 'phone','detail', 'status')
    search_fields = ('product__name', 'customer__first_name', 'customer__last_name', 'address', 'phone', 'status')
