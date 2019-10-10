from django import forms


class UserLoginForm(forms.Form):
    """Form to Log Users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
