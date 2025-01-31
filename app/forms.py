from django import forms
from .models import UserConsent

class ConsentForm(forms.ModelForm):
    class Meta:
        model = UserConsent
        fields = ['consent_given']
        widgets = {
            'consent_given': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'consent_given': 'I consent to data collection and personalized ads',
        }