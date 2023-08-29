from django import forms
from .models import Ticket

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket', 'description']


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket', 'description']