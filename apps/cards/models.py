from django.db import models


class Card(models.Model):
    bank = models.CharField("Banco", max_length=50)
    maturity = models.IntegerField("Vencimento")
    limit = models.FloatField("Limite")

    def __str__(self):
        return self.bank
