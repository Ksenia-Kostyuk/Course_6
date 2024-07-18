from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from mailings.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserModeratorForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('user_blok',)
