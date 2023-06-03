import email
from pickle import FALSE
from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.Form):
    num1 = forms.CharField(label="Value 1", required=False, widget=forms.TextInput(attrs={"class" : "form-control"}))
    num2 = forms.CharField(label="Value 2", widget=forms.TextInput(attrs={"class" : "form-control"}))
    num3 = forms.CharField(label="Value 3", widget=forms.TextInput(attrs={"class" : "form-control"}))
    email = forms.EmailField(required=True)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']