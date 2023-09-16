from django.contrib import admin
from .models import Discount, Earning


@admin.register(Earning)
class EarningAdmin(admin.ModelAdmin):
    list_display = ("earning", "_value")

    def _value(self, obj):
        return f"R${obj.value}"


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("discount", "_value")

    def _value(self, obj):
        return f"R${obj.value}"
