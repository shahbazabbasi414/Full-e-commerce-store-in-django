from django.db import models

class Fabric(models.Model):
  fabric= models.CharField(max_length=20)
  
  def __str__(self):
    return self.fabric
