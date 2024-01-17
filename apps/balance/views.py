from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import EarningForm, DiscountForm
from .models import Earning, Discount
from utils.utils import total_value


def add_earning(request):
    form = EarningForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return render(request, "add-earning.html", context)


def add_discount(request):
    form = DiscountForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return render(request, "add-discount.html", context)


def list_balance():
    earnings = Earning.objects.all()
    discounts = Discount.objects.all()
    total_discounts = total_value(discounts, "value")
    total_balance = total_value(earnings, "value") - total_discounts
    return {
        "earnings": earnings,
        "discounts": discounts,
        "total_discounts": total_discounts,
        "total_balance": total_balance
    }


def render_list_balance():
    return render_to_string("list-balance.html", list_balance())
