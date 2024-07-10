from django.db import models

# Create your models here.


class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    Incident_number_id = models.ForeignKey(
        'Incident.Incident', on_delete=models.CASCADE)
