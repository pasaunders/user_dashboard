from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class add_form(ModelForm):
    password = forms.CharField(label='Password:', min_length=8, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password:', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']


    def clean(self):
        cleaned_data = super(add_form, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('password and confirmaiton must match')


class edit_form(forms.Form):
    pass