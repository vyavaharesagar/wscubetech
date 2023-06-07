from django.urls import path
from . import views

app_name = 'breaks'

urlpatterns = [
    path('', views.break_list, name='break_list'),
    path('create/', views.create_break, name='create_break'), 
]
