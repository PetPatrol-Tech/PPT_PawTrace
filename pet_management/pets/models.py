from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=80)
    score = models.IntegerField(default=100)


    def __str__(self):
        return self.name
