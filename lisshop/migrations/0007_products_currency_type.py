# Generated by Django 3.2 on 2021-05-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lisshop', '0006_auto_20210504_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='currency_type',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]