from django import forms
from .models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['subject', 'template', 'send_time']
        widgets = {'send_time': forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'id_send_time'}),}