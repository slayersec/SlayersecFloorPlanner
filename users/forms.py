from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User




class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        User = get_user_model()
        
        fields = ('email', 'name', 'image','employeeID', 'role', 'phone', 'age', 'position', 'records', 'warnings', 'notes')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        User = get_user_model()
        model = User
        fields = ('email', 'name', 'image','employeeID', 'role', 'phone', 'age', 'position', 'records', 'warnings', 'notes')