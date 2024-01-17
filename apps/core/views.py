from django.shortcuts import render
from apps.bills.views import list_bills, list_invoices, render_list_bills, render_list_invoices
from apps.agreements.views import list_debtors, list_receivers, render_list_debtors, render_list_receivers
from apps.balance.views import list_balance, render_list_balance


def remainder():
    total_bills = list_bills()["total_bills"]
    invoices = list_invoices()
    total_invoices = invoices["total_invoices"] + invoices["total_extra_invoices"]
    total_debtors = list_debtors()["total_debtors"]
    total_receivers = list_receivers()["total_receivers"]
    total_balance = list_balance()["total_balance"]

    total_remainder = sum([total_balance, total_debtors]) - sum([total_bills, total_invoices, total_receivers])

    return format(total_remainder, ".2f")


def home(request):
    context = {
        "balance": render_list_balance(),
        "bills": render_list_bills(),
        "invoices": render_list_invoices(),
        "debtors": render_list_debtors(),
        "receivers": render_list_receivers(),
        "remainder": remainder()
    }
    return render(request, "home.html", context)


def login(request):
    return render(request, "login.html")