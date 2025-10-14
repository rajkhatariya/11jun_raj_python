from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=usignup
        fields='__all__'