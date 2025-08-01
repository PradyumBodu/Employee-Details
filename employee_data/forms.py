from django import forms
from .models import Employees

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['first_name','last_name','email','desig']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'desig': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Designation'}),
        }
