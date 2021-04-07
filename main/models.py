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







        