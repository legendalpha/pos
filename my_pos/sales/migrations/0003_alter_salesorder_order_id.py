# Generated by Django 5.0.2 on 2024-02-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_orderstatus_salesorder_cash_tendered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='order_id',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
