
#! djangonun hazır User modeli
from django.contrib.auth.models import User
#! oluşturduğumuz model
from .models import UserProfile
#! djangonun forms yapısı
from django import forms
#! djangonun User için creation formu
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']


class UserUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
    



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # ! tupple ile dışlama ',' koymamız gerekiyor
        # fields = ['profile_pic', 'bio']
        exclude = ('user',)
        