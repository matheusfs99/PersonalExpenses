from django.contrib import admin
from .models import Debtor, Receiver


@admin.register(Debtor)
class DebtorAdmin(admin.ModelAdmin):
    list_display = ("name", "_value", "billing_date", "_paid")

    def _paid(self, obj):
        if not obj.paid:
            return "Pendente"
        return "Pago"

    def _value(self, obj):
        return f"R${obj.value}"


@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    list_display = ("name", "_value", "payment_date", "_paid")

    def _paid(self, obj):
        if not obj.paid:
            return "Pendente"
        return "Pago"

    def _value(self, obj):
        return f"R${obj.value}"
