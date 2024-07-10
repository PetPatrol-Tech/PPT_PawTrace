from django.db import models
from Residents.models import Resident
# Create your models here.


class Incident(models.Model):
    incident_number = models.AutoField(primary_key=True)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    record_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Incident {self.incident_number}"
