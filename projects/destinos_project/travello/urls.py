from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_destination, name='add_destination'),
    path('list/', views.list_destinations, name='list_destinations'),
    path('edit/<int:id>/', views.edit_destination, name='edit_destination'),
    path('delete/<int:id>/', views.delete_destination, name='delete_destination'),
]
