from django.urls import path

from .views import patient_list, measurement_list, add_measurement

urlpatterns = [
    path('patients/', patient_list, name='patient_list'),
    path('patients/<int:patient_id>/', measurement_list, name='measurement_list'),
    path('patients/<int:patient_id>/add_measurement/', add_measurement, name='add_measurement'),
]
