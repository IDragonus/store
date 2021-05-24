from django import forms
from django.db.models import fields
from .models import Products, Sales, PayType, SalesByProduct, SalesByPayType


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        # fields = ['product_code', 'product_name', 'product_details', 'product_gender', 'product_price', 'product_inventory']


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'
        # fields = ['sale_date', 'pay_method', 'id_product']