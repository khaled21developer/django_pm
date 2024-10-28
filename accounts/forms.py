from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
attrs = {'class': 'form-control'}

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label=_('Username'),  # ترجمة
        widget=forms.TextInput(attrs=attrs)
    )

    password = forms.CharField(
        label=_('Password'),  # ترجمة
        widget=forms.PasswordInput(attrs=attrs)
    )


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        label=_('First Name'),  # ترجمة
        widget=forms.TextInput(attrs=attrs)
    )
    last_name = forms.CharField(
        label=_('Last Name'),  # ترجمة
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label=_('Username'),  # ترجمة
        widget=forms.TextInput(attrs=attrs)
    )
    email = forms.EmailField(
        label=_('Email'),  # ترجمة
        widget=forms.TextInput(attrs=attrs)
    )
    password1 = forms.CharField(
        label=_('Password'),  # ترجمة
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )
    password2 = forms.CharField(
        label=_('Password Confirmation'),  # ترجمة
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email')


class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }