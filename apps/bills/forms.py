from django import forms
from .models import Bill, Invoice


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"
        widgets = {
            "bill": forms.TextInput(attrs={"class": "form-control"}),
            "value": forms.TextInput(attrs={"class": "form-control"}),
            "payment_method": forms.TextInput(attrs={"class": "form-control"}),
            "payment_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "paid": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"
        widgets = {
            "purchase": forms.TextInput(attrs={"class": "form-control"}),
            "is_fixed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "installments": forms.NumberInput(attrs={"class": "form-control"}),
            "installment_value": forms.NumberInput(attrs={"class": "form-control"}),
            "total": forms.NumberInput(attrs={"class": "form-control"}),
            "current_installment": forms.NumberInput(attrs={"class": "form-control"}),
            "card": forms.Select(attrs={"class": "form-select"}),
        }


class InvoiceExtraForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ("purchase", "total", "card")
        widgets = {
            "purchase": forms.TextInput(attrs={"class": "form-control"}),
            "total": forms.NumberInput(attrs={"class": "form-control"}),
            "card": forms.Select(attrs={"class": "form-select"}),
        }

    def save(self, commit=True):
        instance = super(InvoiceExtraForm, self).save(commit=False)
        instance.installments = 1
        instance.installment_value = instance.total
        instance.current_installment = 1
        instance.save()
        return instance


