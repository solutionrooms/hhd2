from django.contrib import admin
from .models import Patient, Carer, Measurement

admin.site.register(Patient)
admin.site.register(Carer)
admin.site.register(Measurement)
