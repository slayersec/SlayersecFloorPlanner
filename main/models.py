from django.db import models

# Create your models here.
class mapData(models.Model):
    mapName = models.CharField(max_length=200)
    data = models.CharField(max_length=20000)
    mapPublished = models.DateTimeField('date published')
    thumbnail = models.ImageField(upload_to = 'thumbnails/')


    def __str__(self):
        return self.mapName
        