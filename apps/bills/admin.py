from django.contrib import admin
from .models import Bill, Invoice


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ("bill", "_value", "payment_date", "_paid")

    def _paid(self, obj):
        if not obj.paid:
            return "Pendente"
        return "Pago"

    def _value(self, obj):
        return f"R${obj.value}"


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "purchase",
        "_is_fixed",
        "_installments",
        "_installment_value",
        "card"
    )

    def _is_fixed(self, obj):
        if obj.is_fixed:
            return "Sim"
        return "Não"
    _is_fixed.short_description = "Fixo?"

    def _installments(self, obj):
        return f"{obj.current_installment}/{obj.installments}"
    _installments.short_description = "Parcelas"

    def _installment_value(self, obj):
        return f"R${obj.installment_value}"

    _installment_value.short_description = "Valor da parcela"
