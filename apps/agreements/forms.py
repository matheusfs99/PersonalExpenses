from django import forms
from .models import Debtor, Receiver


class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = "__all__"
        widgets = {
            "billing_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(DebtorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = "__all__"
        widgets = {
            "payment_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(ReceiverForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
