from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    #name = models.ForeignKey('user.User',on_delete=models.CASCADE)
    image = models.ImageField(blank = True, null = True)
    employeeID = models.TextField()
    role = models.TextField()
    phone = models.TextField()    
    age = models.TextField()
    position = models.TextField()
    records = models.TextField()
    warnings = models.TextField()
    notes = models.TextField()
    userSince = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


# Create your models here.
