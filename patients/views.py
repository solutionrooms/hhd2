from django.shortcuts import render, redirect, get_object_or_404

from .forms import MeasurementForm, PatientForm, CarerCreationForm
from .models import Patient, Measurement
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



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


def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})


def patient_update(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        carer_form = CarerCreationForm(request.POST)
        if user_form.is_valid() and carer_form.is_valid():
            user = user_form.save()
            carer = carer_form.save(commit=False)
            carer.user = user
            carer.save()
            login(request, user)
            return redirect('patient_list')
    else:
        user_form = UserCreationForm()
        carer_form = CarerCreationForm()
    return render(request, 'patients/register.html', {'user_form': user_form, 'carer_form': carer_form})

from django.contrib.auth.views import LoginView

class LoginView(LoginView):
    template_name = 'patients/login.html'