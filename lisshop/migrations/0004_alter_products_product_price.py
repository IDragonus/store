# Generated by Django 3.2 on 2021-05-04 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lisshop', '0003_paytype_sales_salesbypaytype_salesbyproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.CharField(max_length=255),
        ),
    ]