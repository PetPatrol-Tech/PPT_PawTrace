from django.db import models

class Pet(models.Model):
    pet_id= models.AutoField(primary_key=True),
    pet_name=models.CharField(max_length=80),
    pet_age=models.IntegerField(),
    Resident_id=models.IntegerField(),
    pet_catagory=models.CharField(),
    def __str__(self):
        return self.pet_name