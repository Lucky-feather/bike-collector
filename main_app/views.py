from django.shortcuts import render
from .models import Bike
# # Add the following import
# from django.http import HttpResponse

# Define the home view
# def home(request):
#   return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# Create your views here.
def about(request):
  return render(request, 'about.html')

# class Bike:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, type, description, pros, cons):
#     self.type = type
#     self.description = description
#     self.pros = pros
#     self.cons = cons

# bikes = [
#   Bike('Gravel Bike', 'Thicker tires than a road bike but not built for mountain trails.', 'durable', 'slower than a regular road bike' ),
#   Bike('EBike', 'bike with a motor that helps add power to pedaling', 'makes hills easier', 'less exercise' )
# ]

def bikes_index(request):
  bikes = Bike.objects.all()
  return render(request, 'bikes/index.html', {'bikes': bikes })

def home(request):
  return render(request, 'home.html')

