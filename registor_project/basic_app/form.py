from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,URLinput

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','picture')

class URLinputForm(ModelForm):
    class Meta():
        model = URLinput
        fields = ('inputURL_value',)

