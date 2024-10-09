from django.db import models

class Customization(models.Model):
  customization= models.CharField(max_length=20)
  
  def __str__(self):
    return self.customization
