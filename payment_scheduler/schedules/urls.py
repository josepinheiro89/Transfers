from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/agendamentos/', views.create_schedule, name='create_schedule'),
    path('api/', views.list_schedules, name='list_schedules'),
    path('api/agendamento/<int:id>/', views.get_schedule, name='get_schedule'),
    path('api/delete/<int:id>/', views.delete_schedule, name='delete_schedule'),
]