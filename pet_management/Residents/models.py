from django.db import models

# Create your models here.
class Resident(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=11)
    date = models.DateField()
    numOfPets = models.IntegerField(max_length=1)
    state = models.IntegerField(max_length=1)