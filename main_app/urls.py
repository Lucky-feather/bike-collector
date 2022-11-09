from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),

  path('bikes/', views.bikes_user_index, name='bikes_user_index'),
  path('bikes/mybikes', views.bikes_index, name='bikes_index'),
  path('bikes/<int:bike_id>/', views.bikes_detail, name='bikes_detail'),
  path('bikes/create/', views.BikeCreate.as_view(), name='bikes_create'),
  path('bikes/<int:pk>/update/', views.BikeUpdate.as_view(), name='bikes_update'),
  path('bikes/<int:pk>/delete/', views.BikeDelete.as_view(), name='bikes_delete'),
  path('bikes/<int:bike_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('bikes/<int:bike_id>/assoc_gear/<int:gear_id>/', views.assoc_gear, name='assoc_gear'),

  path('gear/create/', views.GearCreate.as_view(), name='gear_create'),
  path('gear/<int:pk>/', views.GearDetail.as_view(), name='gear_detail'),
  path('gear/', views.GearList.as_view(), name='gear_index'),
  path('gear/<int:pk>/update/', views.GearUpdate.as_view(), name='gear_update'),
  path('gear/<int:pk>/delete/', views.GearDelete.as_view(), name='gear_delete'),

]