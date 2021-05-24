from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:productId>/', views.delete_product, name='delete'),
    path('update_product/<int:productId>/', views.update_product, name='update'),
    # Sales views
    path('sales/', views.salesList, name='sales'),
]