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


def detail_earning(request, pk):
    earning = Earning.objects.get(id=pk)
    form = EarningForm(request.POST or None, instance=earning)
    context = {"form": form, "earning": earning}
    return render(request, "hx/detail-earning.html", context)


def update_earning(request, pk):
    earning = Earning.objects.get(id=pk)
    form = EarningForm(request.POST or None, instance=earning)
    context = {"form": form, "earning": earning}
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "hx/earning-hx.html", context)


def delete_earning(request, pk):
    earning = Earning.objects.get(id=pk)
    earning.delete()
    return render(request, "earning-table.html")


def add_discount(request):
    form = DiscountForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return render(request, "add-discount.html", context)


def detail_discount(request, pk):
    discount = Discount.objects.get(id=pk)
    form = DiscountForm(request.POST or None, instance=discount)
    context = {"form": form, "discount": discount}
    return render(request, "hx/detail-discount.html", context)


def update_discount(request, pk):
    discount = Discount.objects.get(id=pk)
    form = DiscountForm(request.POST or None, instance=discount)
    context = {"form": form, "discount": discount}
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "hx/discount-hx.html", context)


def delete_discount(request, pk):
    discount = Discount.objects.get(id=pk)
    discount.delete()
    return render(request, "discount-table.html")


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
