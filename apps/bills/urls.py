from django.urls import path
from .views import add_bill, add_invoice, add_extra_invoice

app_name = "bills"

urlpatterns = [
    path("add-bill/", add_bill, name="add_bill"),
    path("add-invoice/", add_invoice, name="add_invoice"),
    path("add-extra-invoice/", add_extra_invoice, name="add_extra_invoice"),
]
