from django.db import models
from django.urls import reverse
from datetime import date, timedelta

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
  ('O', 'Other')
)
class Gear(models.Model):
  item = models.CharField(max_length=50)
  picture = models.CharField(max_length=200, default=' ')
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

  
  # def recent_work(self):
  #   return self.work_set.filter(
  #     date=date.today()).count()
# /for this above function, I want it to:
# /check the date of the most recent work done
# /compare it to the date 7 days prior to today
# /see if the date of the work done is as recent or more recent.


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

# Add the gear model