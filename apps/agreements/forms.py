from django import forms
from .models import Debtor, Receiver


class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = "__all__"


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = "__all__"
