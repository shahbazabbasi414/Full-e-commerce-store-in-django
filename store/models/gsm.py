from django.db import models

class GSM(models.Model):
  GSM = models.CharField(max_length=20)
  
  def __str__(self):
    return self.GSM
