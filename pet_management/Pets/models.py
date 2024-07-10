from django.db import models


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=80)
    pet_age = models.IntegerField()
    resident = models.ForeignKey(
        'Residents.Resident', on_delete=models.CASCADE)
    pet_category = models.CharField(max_length=80, default="unknown")
