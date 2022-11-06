from django.db import models
from django.urls import reverse

class Bike(models.Model):
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  pros = models.TextField(max_length=250)
  cons = models.TextField(max_length=250)

  def __str__(self):
    return self.type
  
  def get_absolute_url(self):
    return reverse('bikes_detail', kwargs={'bike_id': self.id})