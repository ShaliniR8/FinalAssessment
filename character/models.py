from django.db import models

# Create your models here.
class Character(models.Model):
     name = models.CharField(max_length= 100, null = False, blank=False)
     description = models.TextField(max_length= 400, null = True, blank= True)