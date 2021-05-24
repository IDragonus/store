from django.contrib import admin
from .models import Products, Sales, PayType, SalesByProduct, SalesByPayType


admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(PayType)
admin.site.register(SalesByProduct)
admin.site.register(SalesByPayType)