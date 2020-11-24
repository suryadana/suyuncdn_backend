from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    is_banned = models.BooleanField(default=False)
