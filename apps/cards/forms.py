from django import forms
from .models import Card


class CardForms(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
        widgets = {
            "bank": forms.TextInput(attrs={"class": "form-control"}),
            "maturity": forms.TextInput(attrs={"class": "form-control"}),
            "limit": forms.NumberInput(attrs={"class": "form-control"})
        }
