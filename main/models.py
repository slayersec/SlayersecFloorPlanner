from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

user = User.objects.get(id=2)
user_email = user.email

# Create your models here.
class mapdata(models.Model):
    mapName = models.CharField(max_length=200)
    data = models.CharField(max_length=20000)
    mapPublished = models.DateTimeField('date published')
    def __str__(self):
        return self.mapName

class users(models.Model):
    name = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank = True, null = True)
    employeeID = models.TextField()
    role = models.TextField()
    email = auth_user.objects.get(id__exact=2)
    phone = models.TextField()    
    age = models.TextField()
    position = models.TextField()
    records = models.TextField()
    warnings = models.TextField()
    notes = models.TextField()
    userSince = models.DateTimeField(default=timezone.now)





        