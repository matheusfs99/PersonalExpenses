from django.urls import path
from .views import *

app_name = "agreements"

urlpatterns = [
    path("add-debtor/", add_debtor, name="add_debtor"),
    path("add-receiver/", add_receiver, name="add_receiver"),
    path("debtor/<int:pk>/", detail_debtor, name="detail_debtor"),
    path("update-debtor/<int:pk>/", update_debtor, name="update_debtor"),
    path("receiver/<int:pk>/", detail_receiver, name="detail_receiver"),
    path("update-receiver/<int:pk>/", update_receiver, name="update_receiver"),
    path("delete-receiver/<int:pk>/", delete_receiver, name="delete_receiver"),
    path("delete-debtor/<int:pk>/", delete_debtor, name="delete_debtor"),
]
