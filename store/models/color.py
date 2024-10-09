from django.db import models

class Color(models.Model):
  color= models.CharField(max_length=20)
  
  def __str__(self):
    return self.color
