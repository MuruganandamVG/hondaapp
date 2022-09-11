from django.forms import ModelForm,TextInput,PasswordInput
from django import forms
from .models import Booking_by_customer,staff,Two_wheeler
class Booking_by_customer(ModelForm):
    class Meta:
        model=Booking_by_customer
        fields="__all__"
class staffregistration(ModelForm):
    class Meta:
        model=staff
        fields="__all__"
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter your username'
                }),
            'staffname': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter staffname'
                }),
            'staffAddress': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter staffaddress'
                }),
            'staffpancard': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter staffpancard'
                }),
            'staffaadharcardno': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter staffaadharcardno'
                }),
            'staffphoneno': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter staffphoneno'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter password'
                })
        }

class AddTwoWheeler(ModelForm):
    class Meta:
        model=Two_wheeler
        fields=['title','Totalstock','Available']
