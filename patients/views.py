from django.shortcuts import render

from django.shortcuts import render
from .forms import MeasurementForm
from .models import Patient, Measurement


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})


def measurement_list(request, patient_id):
    measurements = Measurement.objects.filter(patient_id=patient_id)
    return render(request, 'patients/measurement_list.html', {
        'measurements': measurements,
        'patient_id': patient_id,
    })


def add_measurement(request, patient_id):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('measurement_list', patient_id=patient_id)
    else:
        form = MeasurementForm(initial={'patient': patient_id, 'carer': request.user.id})
    return render(request, 'patients/add_measurement.html', {'form': form, 'patient_id': patient_id})

