import datetime
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_birth_date(self):
        date = self.cleaned_data.get('birth_date')
        today = datetime.date.today()
        if date.year >= today.year - 18:
            raise forms.ValidationError("You must grow up")
        return date

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'fill-container'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'fill-container'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError(message='Invalid username or password',
                                        code='invalid_login')
