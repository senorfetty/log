from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Mkubwa, Customer



class RegForm(UserCreationForm):
    first_name= forms.CharField(max_length=100,required=True, help_text='Required.')
    last_name= forms.CharField(max_length=100, required=True, help_text='Required.')
    email= forms.EmailField(max_length=30, required=True, help_text='Required.')
    phone_number= forms.CharField(max_length=15)


    class Meta:
        model= Customer
        fields= ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')

    
class AdminForm(UserCreationForm):
    email= forms.EmailField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = Mkubwa
        fields= ('username','first_name', 'last_name', 'email','password1', 'password2')