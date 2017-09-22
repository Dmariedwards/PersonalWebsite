from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from webmodels.models import Section, User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        """ this line sets your form's method to post"""
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', u'Submit', css_class='btn btn-success'))
    username = forms.CharField(label="Username", 
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(
        label="Password", 
        max_length=30, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
