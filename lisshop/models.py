from django.db import models
from django.db.models.fields import CharField, DateField
from django.forms.utils import to_current_timezone


class Products(models.Model):
    product_code = models.IntegerField(null=False)
    product_name = models.CharField(max_length=255, null=False)
    product_details = models.CharField(max_length=255, null=False)
    product_gender = models.CharField(max_length=1, null=False)
    product_price = models.DecimalField(max_digits=30, decimal_places=2, null= False)
    currency_type = models.CharField(max_length=3, null=False)
    product_inventory = models.IntegerField(null=False)

    def __str__(self):
        return self.product_name


class Sales(models.Model):
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    sale_date = models.DateField(null=False)
    pay_method = models.CharField(max_length=20)

    def __str__(self):
        return Sales


class PayType(models.Model):
    description = CharField(max_length=50)

    def __str__(self):
        return self.description


class SalesByProduct(models.Model):
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    id_sales = models.ForeignKey(Sales, on_delete=models.CASCADE)


class SalesByPayType(models.Model):
    pay_type = models.ForeignKey(PayType, on_delete=models.CASCADE)
    id_sales = models.ForeignKey(Sales, on_delete=models.CASCADE)