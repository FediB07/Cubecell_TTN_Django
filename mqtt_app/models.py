from django.db import models

# Create your models here.
class Data(models.Model):
    donnée=models.CharField(max_length=500)