# Generated by Django 3.2 on 2021-05-04 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lisshop', '0002_alter_products_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateField(auto_now=True)),
                ('pay_method', models.CharField(max_length=20)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lisshop.products')),
            ],
        ),
        migrations.CreateModel(
            name='SalesByProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lisshop.products')),
                ('id_sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lisshop.sales')),
            ],
        ),
        migrations.CreateModel(
            name='SalesByPayType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lisshop.sales')),
                ('pay_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lisshop.paytype')),
            ],
        ),
    ]
