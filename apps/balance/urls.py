from django.urls import path
from .views import add_earning, add_discount

app_name = "balance"

urlpatterns = [
    path("add-earning", add_earning, name="add_earning"),
    path("add-discount", add_discount, name="add_discount"),
]
