from django import forms
from .models import Flight

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class FlightForm(forms.ModelForm):
    class Meta:
        Model = Flight
        fields = ['DepAirport', 'DepDate', 'DepTime', 'ArrAirport', 'ArrDate', 'ArrTime']


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'