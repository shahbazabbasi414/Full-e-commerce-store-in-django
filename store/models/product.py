from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000, default='')
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/', null=True, blank=True)

    
    @staticmethod
    def get_Products_by_id(ids):
        return Product.objects.filter(id__in = ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    
    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all();
        
@staticmethod
def get_Products_by_id(ids):
    products = Product.objects.filter(id__in=ids)
    print(f"Retrieved products: {products}")  # Debug statement
    return products
        