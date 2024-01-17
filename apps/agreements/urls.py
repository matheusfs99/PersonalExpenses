from django.urls import path
from .views import add_debtor, add_receiver

app_name = "agreements"

urlpatterns = [
    path("add-debtor/", add_debtor, name="add_debtor"),
    path("add-receiver/", add_receiver, name="add_receiver"),
]
