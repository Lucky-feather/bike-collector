from django.db import models

class Bike(models.Model):
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  pros = models.TextField(max_length=250)
  cons = models.TextField(max_length=250)

  def __str__(self):
    return self.type
''