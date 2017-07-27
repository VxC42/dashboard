from django import forms
from .models import User


class RegForm(forms.ModelForm):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(
        min_length=7,
        widget = forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        min_length=7,
        widget = forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
        )

    def clean(self):
        cleaned = self.cleaned_data
        print cleaned
        if cleaned['password'] != cleaned['confirm_password']:
            raise forms.ValidationError("Passwords do not match")

class SigninForm(forms.ModelForm):
    email = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )
