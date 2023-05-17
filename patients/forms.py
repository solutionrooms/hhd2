from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils import timezone

from crispy_forms.layout import Layout, Field

from .models import Measurement


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


