from django.db import models

class Destinations(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(upload)

# Create your models here.
