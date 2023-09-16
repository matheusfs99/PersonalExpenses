from django.db import models


class Earning(models.Model):
    earning = models.CharField("Ganho", max_length=50)
    value = models.FloatField("Valor")


class Discount(models.Model):
    discount = models.CharField("Desconto", max_length=50)
    value = models.FloatField("Valor")
