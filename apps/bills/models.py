from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Bill(models.Model):
    bill = models.CharField("Conta", max_length=50)
    value = models.FloatField("Valor")
    payment_method = models.CharField("Forma de pagamento", max_length=100)
    payment_date = models.DateField("Data de pagamento", null=True, blank=True)
    paid = models.BooleanField("Pago", default=False)


class Invoice(models.Model):
    purchase = models.CharField("Compra", max_length=50)
    is_fixed = models.BooleanField("É fixo?", default=False)
    installments = models.PositiveSmallIntegerField(
        "Parcelas", validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    installment_value = models.FloatField("Valor da parcela")
    total = models.FloatField("Valor total", null=True, blank=True)
    current_installment = models.PositiveSmallIntegerField(
        "Parcela atual", validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    card = models.ForeignKey("cards.Card", on_delete=models.CASCADE, verbose_name="Cartão")
