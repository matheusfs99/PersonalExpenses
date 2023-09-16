# Generated by Django 4.2.5 on 2023-09-16 05:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.CharField(max_length=50, verbose_name='Conta')),
                ('value', models.FloatField(verbose_name='Valor')),
                ('payment_method', models.CharField(max_length=100, verbose_name='Forma de pagamento')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='Data de pagamento')),
                ('paid', models.BooleanField(default=False, verbose_name='Pago')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.CharField(max_length=50, verbose_name='Compra')),
                ('is_fixed', models.BooleanField(default=False, verbose_name='É fixo?')),
                ('installments', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Parcelas')),
                ('installment_value', models.FloatField(verbose_name='Valor da parcela')),
                ('total', models.FloatField(blank=True, null=True, verbose_name='Valor total')),
                ('current_installment', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Parcela atual')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.card', verbose_name='Cartão')),
            ],
        ),
    ]
