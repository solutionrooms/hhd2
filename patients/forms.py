from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils import timezone

from crispy_forms.layout import Layout, Field

from .models import Measurement, Patient, Carer


class MeasurementForm(forms.ModelForm):
    measurement_timestamp = forms.DateTimeField(initial=timezone.now,
                                                widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Measurement
        fields = ['patient', 'measurement_timestamp','weight_grams', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('measurement_timestamp', css_class='col-12 col-sm-6'),
            Field('weight_grams', css_class='col-12 col-sm-6'),
            Field('notes', css_class='col-12'),
        )
        self.helper.add_input(Submit('submit', 'Save measurement'))


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'finder_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'age_years': forms.NumberInput(attrs={'class': 'form-control'}),
            'wants_back': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'current_weather': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
            'cold_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fly_strike_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'wounds_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sneezing_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'dehydrated_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'maggots_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limping_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'snotty_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'underweight_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ticks_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'smell_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limp_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fleas_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pus_or_infection': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'course_of_action': forms.Textarea(attrs={'class': 'form-control'}),
            'microchip': forms.TextInput(attrs={'class': 'form-control'}),
            'poo_sample': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'poo_parasites': forms.TextInput(attrs={'class': 'form-control'}),
            'fluids_given': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fluid_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'vet_needed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'incubator_flag': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'incubator_starting_temp_c': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'patient_status': forms.TextInput(attrs={'class': 'form-control'}),
            'inserted_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class CarerCreationForm(forms.ModelForm):
    class Meta:
        model = Carer
        fields = ['full_name', 'address', 'phone_number_home', 'phone_number_mobile', 'opted_out', 'carer_status_id']
