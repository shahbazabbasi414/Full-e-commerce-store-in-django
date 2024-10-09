from django.db import models
from .category import Category
from .material import Material
from .size import Size
from .customization import Customization
from .type import Type
from .color import Color
from .fabric import Fabric
from .gsm import GSM

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    materials = models.ManyToManyField(Material, blank=True)
    sizes = models.ManyToManyField(Size, blank=True)
    customizations = models.ManyToManyField(Customization, blank=True)
    types = models.ManyToManyField(Type, blank=True)
    colors = models.ManyToManyField(Color, blank=True)
    fabrics = models.ManyToManyField(Fabric, blank=True)
    gsms = models.ManyToManyField(GSM, blank=True)
    
    description = models.CharField(max_length=1000, default='')
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    
    def __str__(self):
        return self.name 
    
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
            return Product.objects.all()
        