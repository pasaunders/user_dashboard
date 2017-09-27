"""Forms for gathering login and registration information."""


from django import forms


class register_form(forms.Form):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name:', min_length=2, max_length=60)
    last_name = forms.CharField(label='Last Name:', min_length=2, max_length=60)
    password = forms.CharField(label='Password:', min_length=8, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password:', widget=forms.PasswordInput())


class signin_form(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password:', widget=forms.PasswordInput())
