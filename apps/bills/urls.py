from django.urls import path
from .views import (
    add_bill, add_invoice, add_extra_invoice,
    detail_bill, update_bill, detail_invoice,
    update_invoice, detail_extra_invoice, update_extra_invoice
)

app_name = "bills"

urlpatterns = [
    path("add-bill/", add_bill, name="add_bill"),
    path("add-invoice/", add_invoice, name="add_invoice"),
    path("add-extra-invoice/", add_extra_invoice, name="add_extra_invoice"),
    path("bill/<int:pk>/", detail_bill, name="detail_bill"),
    path("update-bill/<int:pk>/", update_bill, name="update_bill"),
    path("invoice/<int:pk>/", detail_invoice, name="detail_invoice"),
    path("update-invoice/<int:pk>/", update_invoice, name="update_invoice"),
    path("extra-invoice/<int:pk>/", detail_extra_invoice, name="detail_extra_invoice"),
    path("update-extra-invoice/<int:pk>/", update_extra_invoice, name="update_extra_invoice"),
]
