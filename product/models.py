from unicodedata import name
from django.db import models

# Create your models here.
class product(models.Model):
    name        = models.TextField()
    price       = models.TextField()
    summary     =   models.TextField()