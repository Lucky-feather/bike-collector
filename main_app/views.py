from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bike, Gear
from .forms import MaintenanceForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bikes_index(request):
  bikes = Bike.objects.all()
  return render(request, 'bikes/index.html', {'bikes': bikes })

def bikes_detail(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  maintenance_form = MaintenanceForm()
  return render(request, 'bikes/detail.html', {
    'bike' : bike, 'maintenance_form' : maintenance_form })

class BikeCreate(CreateView):
  model = Bike
  fields = ['type', 'color', 'description']

class BikeUpdate(UpdateView) :
  model = Bike
  fields = ['type', 'color', 'description']

class BikeDelete(DeleteView) :
  model = Bike
  success_url = '/bikes/'

def add_maintenance(request, bike_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.bike_id = bike_id
    new_maintenance.save()
  return redirect('bikes_detail', bike_id=bike_id)

class GearCreate(CreateView) :
  model = Gear
  fields = '__all__'

class GearList(ListView):
  model = Gear

class GearDetail(DetailView):
  model = Gear

class GearUpdate(UpdateView):
  model = Gear
  fields = '__all__'

class GearDelete(DeleteView):
  model = Gear
  success_url = '/gear/'