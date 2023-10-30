
from django.urls import path
from . import views

app_name = 'temperature_humidity'

urlpatterns = [
    path('', views.input_data, name='input_data'),
    path('display/', views.display_data, name='display_data'),
     # Define the 'delete_row' URL pattern
    path('delete_row/', views.delete_row, name='delete_row'),
]
