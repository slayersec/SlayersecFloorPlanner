from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User




class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'name', 'image','employeeID', 'role', 'phone', 'age', 'position', 'records', 'warnings', 'notes')
    

class ProfileCustomizeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm):
        model = User
        fields = ('image', 'role', 'phone', 'age', 'notes')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'name', 'image','employeeID', 'role', 'phone', 'age', 'position', 'records', 'warnings', 'notes')
        