from django.forms import ModelForm
from restaurant.models import Bookings
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create the form class.
class BookingForm(ModelForm):
    class Meta:
        model = Bookings
        # fields = ["pub_date", "headline", "content", "reporter"]
        exclude = ["user", "approved"]

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)