from django.db import models


class Debtor(models.Model):
    name = models.CharField("Nome", max_length=100)
    value = models.FloatField("Valor")
    reason = models.CharField("Motivo", max_length=255)
    billing_date = models.DateField("Data de cobrança")
    paid = models.BooleanField("Pago", default=False)


class Receiver(models.Model):
    name = models.CharField("Nome", max_length=100)
    value = models.FloatField("Valor")
    reason = models.CharField("Motivo", max_length=255)
    payment_date = models.DateField("Data de pagamento")
    paid = models.BooleanField("Pago", default=False)
