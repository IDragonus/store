# Generated by Django 3.2 on 2021-05-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lisshop', '0005_auto_20210504_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='products_currency',
        ),
        migrations.AddField(
            model_name='products',
            name='product_gender',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
