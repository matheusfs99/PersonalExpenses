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


def detail_debtor(request, pk):
    debtor = Debtor.objects.get(id=pk)
    form = DebtorForm(request.POST or None, instance=debtor)
    context = {"form": form, "debtor": debtor}
    return render(request, "hx/detail-debtor.html", context)


def update_debtor(request, pk):
    debtor = Debtor.objects.get(id=pk)
    form = DebtorForm(request.POST or None, instance=debtor)
    context = {"form": form, "debtor": debtor}
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "hx/debtor-hx.html", context)


def delete_debtor(request, pk):
    debtor = Debtor.objects.get(id=pk)
    debtor.delete()
    return render(request, "debtors-table.html")


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


def detail_receiver(request, pk):
    receiver = Receiver.objects.get(id=pk)
    form = ReceiverForm(request.POST or None, instance=receiver)
    context = {"form": form, "receiver": receiver}
    return render(request, "hx/detail-receiver.html", context)


def update_receiver(request, pk):
    receiver = Receiver.objects.get(id=pk)
    form = ReceiverForm(request.POST or None, instance=receiver)
    context = {"form": form, "receiver": receiver}
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "hx/receiver-hx.html", context)


def delete_receiver(request, pk):
    receiver = Receiver.objects.get(id=pk)
    receiver.delete()
    return render(request, "receivers-table.html")


def list_receivers():
    receivers = Receiver.objects.filter(paid=False)
    total_receivers = total_value(receivers, "value")
    return {
        "receivers": receivers,
        "total_receivers": total_receivers,
    }


def render_list_receivers():
    return render_to_string("list-receivers.html", list_receivers())