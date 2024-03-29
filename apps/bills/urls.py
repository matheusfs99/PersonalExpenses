from django.urls import path
from .views import *

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
    path("delete-bill/<int:pk>/", delete_bill, name="delete_bill"),
    path("delete-invoice/<int:pk>/", delete_invoice, name="delete_invoice"),
    path("delete-extra-invoice/<int:pk>/", delete_extra_invoice, name="delete_extra_invoice"),
]
