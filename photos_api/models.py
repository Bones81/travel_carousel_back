from django.db import models

# Create your models here.
class Photo(models.Model):
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    comments = models.CharField(max_length=500)
    image_file = models.ImageField(upload_to='photos/%Y/%m/%d')