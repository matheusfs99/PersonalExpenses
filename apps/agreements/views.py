from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import DebtorForm, ReceiverForm
from .models import Debtor, Receiver
from utils.utils import total_value


def add_debtor(request):
    form = DebtorForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return render(request, "add-debtor.html", context)


def list_debtors():
    debtors = Debtor.objects.filter(paid=False)
    total_debtors = total_value(debtors, "value")
    return {
        "debtors": debtors,
        "total_debtors": total_debtors,
    }


def render_list_debtors():
    return render_to_string("list-debtors.html", list_debtors())


def add_receiver(request):
    form = ReceiverForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return render(request, "add-receiver.html", context)


def list_receivers():
    receivers = Receiver.objects.filter(paid=False)
    total_receivers = total_value(receivers, "value")
    return {
        "receivers": receivers,
        "total_receivers": total_receivers,
    }


def render_list_receivers():
    return render_to_string("list-receivers.html", list_receivers())