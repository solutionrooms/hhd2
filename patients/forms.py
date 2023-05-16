from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils import timezone


from .models import Measurement


class MeasurementForm(forms.ModelForm):
    measurement_timestamp = forms.DateTimeField(initial=timezone.now,
                                                widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Measurement
        fields = ['patient', 'weight_grams', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save measurement'))


