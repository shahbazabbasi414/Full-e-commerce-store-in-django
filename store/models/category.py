from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    
    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    @staticmethod
    def get_all_category_by_id():
        return Category.objects.all()
        

    def __str__(self):
        return self.name