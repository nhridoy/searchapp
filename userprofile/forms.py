from django import forms
from userprofile.models import Profile, User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password',)
