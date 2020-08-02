from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Ваш пароль')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Ваш пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторить пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        labels = {'username': 'Ваш никнейм', 'first_name': 'Ваше имя', 'email': 'Ваш e-mail'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {'first_name': 'Ваше имя', 'last_name': 'Ваше фамилие', 'email': 'Ваш e-mail'}


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
        labels = {'date_of_birth': 'Дата рождения', 'photo': 'Аватар'}
