from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
import re

class Register_Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username', 'autocomplete': 'off'}), max_length='30')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}), max_length='30')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password (Again)'}), max_length='30')

    
    def clean(self):
        cleaned_data = super().clean()
        rgx = r"^[A-Za-z][A-Za-z0-9_]{5,29}$"  # pattern for validation
        username = cleaned_data['username']
        user = User.objects.filter(username=username)

        if user:
            raise forms.ValidationError('Username is already taken!')
            return 

        if not bool(re.match(rgx, username)):
            raise forms.ValidationError('Invalid username!')
            return

        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match!')
            return
        
        if not bool(re.match(rgx, password1)):
            raise forms.ValidationError('Invalid password!')
            return


class Login_Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username', 'autocomplete': 'off'}), max_length='30')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}), max_length='30')


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        password = cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid credentials!')
            return
