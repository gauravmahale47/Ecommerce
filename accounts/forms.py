from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django import forms

class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'title':'First Name', 'placeholder':'Enter First Name', 'class':'border border-dark text-dark form-control mb-2'}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'title':'Last Name', 'placeholder':'Enter Last Name', 'class':'border border-dark text-dark form-control mb-2'}))
    mobileno = forms.IntegerField(label="Mobile No", widget=forms.NumberInput(attrs={'title':'Mobile No', 'placeholder':'10 Digit\'s Number', 'class':'border border-dark text-dark form-control mb-2'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'title':'Enter Email Id', 'placeholder':'Email Address', 'class':'border border-dark text-dark form-control mb-2'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'title':'Username', 'placeholder':'Enter Username', 'class':'border border-dark text-dark form-control mb-2'}))
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'title':'Password', 'placeholder':'Enter Password', 'class':'border border-dark text-dark form-control mb-2'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'title':'Confirm Password', 'placeholder':'Confirm Password', 'class':'border border-dark text-dark form-control mb-2'}))
    class Meta:
        model = MyUser
        fields= ('first_name',
                 'last_name',
                 'mobileno',
                 'email',
                 'username',
                 'password1',
                 'password2')

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'title':'Username','placeholder':'Enter Username', 'class':'border border-dark text-dark form-control mb-2 ms-2 '}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'title':'Password','placeholder':'Enter Password', 'class':'border border-dark text-dark form-control mb-2 ms-2 '}),
    )