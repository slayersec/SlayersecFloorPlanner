from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class mapdata(models.Model):
    mapName = models.CharField(max_length=200)
    data = models.CharField(max_length=20000)
    mapPublished = models.DateTimeField('date published')
    def __str__(self):
        return self.mapName

class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    #name = models.CharField(max_length=254, null=True, blank=True)
    name = models.ForeignKey('auth.User',on_delete=models.CASCADE)
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





        