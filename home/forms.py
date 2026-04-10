from django import forms
from .models import Accounts

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Accounts
        fields="__all__"
        exclude=['pin','balance']