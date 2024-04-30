from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# form for registering, used to create a user object
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, 
        help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


