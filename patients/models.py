from django.db import models

from django.db import models


class Patient(models.Model):
    patient_name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)
    patient_status = models.TextField()
    inserted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.patient_name}"


class Carer(models.Model):
    full_name = models.TextField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number_home = models.TextField(blank=True, null=True)
    phone_number_mobile = models.TextField(blank=True, null=True)
    opted_out = models.BooleanField(default=False)
    carer_status_id = models.IntegerField()
    inserted_at = models.DateTimeField(auto_now_add=True)


class Measurement(models.Model):
    measurement_timestamp = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    carer = models.ForeignKey(Carer, on_delete=models.CASCADE)
    weight_grams = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    inserted_at = models.DateTimeField(auto_now_add=True)

