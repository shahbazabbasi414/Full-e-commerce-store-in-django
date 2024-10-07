from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    def get_children(self):
        return self.children.all()

    def __str__(self):
        return self.name
