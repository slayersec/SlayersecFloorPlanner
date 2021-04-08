from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User




class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        #model = User
        User = get_user_model()
        fields = ('username','email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        #model = User
        User = get_user_model()
        fields = ('username','email')