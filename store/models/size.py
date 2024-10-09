from django.db import models

class Size(models.Model):
  size= models.CharField(max_length=20)
  
  def __str__(self):
    return self.size
