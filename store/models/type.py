from django.db import models

class Type(models.Model):
  type= models.CharField(max_length=20)
  
  def __str__(self):
    return self.type
