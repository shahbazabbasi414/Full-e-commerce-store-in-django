from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
        ('Completed', 'Completed'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.datetime.today)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=11, default='', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f'Order {self.id} by {self.customer}'

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer):
        return Order.objects.filter(customer=customer).order_by('-date')
