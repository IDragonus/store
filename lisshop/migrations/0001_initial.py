# Generated by Django 3.2 on 2021-05-04 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.IntegerField()),
                ('product_name', models.CharField(max_length=255)),
                ('product_details', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('product_inventory', models.IntegerField()),
            ],
        ),
    ]
