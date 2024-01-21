from django import forms
from .models import Earning, Discount


class EarningForm(forms.ModelForm):
    class Meta:
        model = Earning
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EarningForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(DiscountForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
