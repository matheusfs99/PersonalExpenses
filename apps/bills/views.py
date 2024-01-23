from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.db.models import Q
from .forms import BillForm, InvoiceForm, InvoiceExtraForm
from .models import Bill, Invoice
from utils.utils import total_value


def add_bill(request):
    form = BillForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return render(request, "add-bill.html", context)


def detail_bill(request, pk):
    bill = Bill.objects.get(id=pk)
    form = BillForm(request.POST or None, instance=bill)
    context = {"form": form, "bill": bill}
    return render(request, "hx/detail-bill.html", context)


def update_bill(request, pk):
    bill = Bill.objects.get(id=pk)
    form = BillForm(request.POST or None, instance=bill)
    context = {"form": form, "bill": bill}
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "hx/bill-hx.html", context)


def delete_bill(request, pk):
    bill = Bill.objects.get(id=pk)
    bill.delete()
    return render(request, "bills-table.html")


def list_bills():
    bills = Bill.objects.all()
    total_bills = total_value(bills, "value")
    return {
        "bills": bills,
        "total_bills": total_bills,
    }


def render_list_bills():
    return render_to_string("list-bills.html", list_bills())


def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return render(request, "add-invoice.html", context)


def detail_invoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    form = InvoiceForm(request.POST or None, instance=invoice)
    context = {"form": form, "invoice": invoice}
    return render(request, "hx/detail-invoice.html", context)


def update_invoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    form = InvoiceForm(request.POST or None, instance=invoice)
    context = {"form": form, "invoice": invoice}
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "hx/invoice-hx.html", context)


def delete_invoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    invoice.delete()
    return render(request, "invoices-table.html")


def add_extra_invoice(request):
    form = InvoiceExtraForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return render(request, "add-invoice.html", context)


def detail_extra_invoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    form = InvoiceExtraForm(request.POST or None, instance=invoice)
    context = {"form": form, "invoice": invoice}
    return render(request, "hx/detail-extra-invoice.html", context)


def update_extra_invoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    form = InvoiceExtraForm(request.POST or None, instance=invoice)
    context = {"form": form, "invoice": invoice}
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "hx/extra-invoice-hx.html", context)


def delete_extra_invoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    invoice.delete()
    return render(request, "extra-invoices-table.html")


def list_invoices():
    invoices = Invoice.objects.filter(Q(is_fixed=True) | (Q(is_fixed=False) & Q(installments__gt=1)))
    total_invoices = total_value(invoices, "installment_value")
    extra_invoices = Invoice.objects.filter(Q(is_fixed=False) & Q(installments=1))
    total_extra_invoices = total_value(extra_invoices, "installment_value")
    return {
        "invoices": invoices,
        "total_invoices": total_invoices,
        "extra_invoices": extra_invoices,
        "total_extra_invoices": total_extra_invoices,
    }


def render_list_invoices():
    return render_to_string("list-invoices.html", list_invoices())
