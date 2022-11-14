from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from django.contrib.auth.models import User

WORK = (
  ('T', 'Air Up Tires'),
  ('G', 'Grease Chain'),
  ('C', 'Check Brakes')
)

TYPE = (
  ('E', 'E-Bike'),
  ('R', 'Road Bike'),
  ('G', 'Gravel Bike'),
  ('H', 'Hybrid Bike'),
  ('M', 'Mountain Bike'),
  ('T', 'Touring Bike'),
  ('O', 'Unique Bike')
)
class Gear(models.Model):
  item = models.CharField(max_length=50)
  picture = models.CharField(max_length=200, default='paste link to an image of item ')
  details = models.CharField(max_length=200)
  def __str__(self):
    return self.item
  def get_absolute_url(self):
    return reverse('gear_detail', kwargs={'pk': self.id})

class Bike(models.Model):
  type = models.CharField(
    max_length=1,
    choices=TYPE,
    default=TYPE[0][0]
  )
  color = models.CharField(max_length=20, default='')
  description = models.TextField(max_length=250)
  gear = models.ManyToManyField(Gear)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


  def recent_work(self):
    output = False
    for num in range(0,31):
      if(self.maintenance_set.filter(date=datetime.today()-timedelta(days=num)).count() > 0):
        output = True
    print(output)
    return output

  def __str__(self):
    return self.type
  
  def get_absolute_url(self):
    return reverse('bikes_detail', kwargs={'bike_id': self.id})

class Maintenance(models.Model):
  date = models.DateField()
  work = models.CharField(
    max_length=1,
    choices=WORK,
    default=WORK[0][0]
  )
  bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
  
  def __str__(self): 
    return f"{self.get_work_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
