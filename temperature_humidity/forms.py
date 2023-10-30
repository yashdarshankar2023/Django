
from django import forms
from .models import TemperatureHumidity

class TemperatureHumidityForm(forms.ModelForm):
    class Meta:
        model = TemperatureHumidity
        fields = ['temperature', 'humidity']
