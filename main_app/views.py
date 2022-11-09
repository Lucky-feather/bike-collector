from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Bike, Gear
from .forms import MaintenanceForm


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def bikes_index(request):
  bikes = Bike.objects.all()
  return render(request, 'bikes/index.html', {'bikes': bikes })

def bikes_user_index(request):
  bikes = Bike.objects.filter(user=request.user)
  return render(request, 'bikes/index.html', {'bikes': bikes })

def bikes_detail(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  gear_bike_doesnt_have = Gear.objects.exclude(id__in = bike.gear.all().values_list('id'))
  maintenance_form = MaintenanceForm()
  return render(request, 'bikes/detail.html', {
    'bike' : bike, 'maintenance_form' : maintenance_form, 'gear': gear_bike_doesnt_have })

class BikeCreate(CreateView):
  model = Bike
  fields = ['type', 'color', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

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

def assoc_gear(request, bike_id, gear_id):
  Bike.objects.get(id=bike_id).gear.add(gear_id)
  return redirect('bikes_detail', bike_id=bike_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('bikes_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
