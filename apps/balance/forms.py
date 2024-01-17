from django import forms
from .models import Earning, Discount


class EarningForm(forms.ModelForm):
    class Meta:
        model = Earning
        fields = "__all__"


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = "__all__"
