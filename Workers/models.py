from django.db import models

# Create your models here.
class Workers(models.Model):
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    birth_date=models.DateField()
    jobs=models.CharField(max_length=30)