from django import forms

# Model
from django.contrib.auth.models import User
from accounts.models import Profile


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']
