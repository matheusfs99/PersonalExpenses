from django.urls import path
from .views import *

app_name = "balance"

urlpatterns = [
    path("add-earning/", add_earning, name="add_earning"),
    path("add-discount/", add_discount, name="add_discount"),
    path("earning/<int:pk>/", detail_earning, name="detail_earning"),
    path("update-earning/<int:pk>/", update_earning, name="update_earning"),
    path("discount/<int:pk>/", detail_discount, name="detail_discount"),
    path("update-discount/<int:pk>/", update_discount, name="update_discount"),
    path("delete-discount/<int:pk>/", delete_discount, name="delete_discount"),
    path("delete-earning/<int:pk>/", delete_earning, name="delete_earning"),
]
