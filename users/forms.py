from django import forms
from .models import User

class PatientRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class':'form-control',
        'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter First Name'
                }),
            'last_name': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
                }),
            'email': forms.EmailInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Email Address'
                }),
            'username': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Username'
                }),
            'password': forms.PasswordInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Password'
                })
        }

class ConsultantRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class':'form-control',
        'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'qualification', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter First Name'
                }),
            'last_name': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
                }),
            'email': forms.EmailInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Email Address'
                }),
            'username': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Username'
                }),
            'password': forms.PasswordInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Password'
                }),
            'qualification': forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter Qualification'
            })
        }

