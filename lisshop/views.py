from django.shortcuts import render, redirect
from .models import Products, Sales
from .forms import ProductsForm

def home(request):
    products = Products.objects.all()
    context = { 'products' : products }
    return render(request, 'lisshop/home.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ProductsForm()
    
    context = { 'form' : form }
    return render(request, 'lisshop/add_product.html', context)


def delete_product(request, productId):
    product = Products.objects.get(id=productId)
    product.delete()
    return redirect('home')


def update_product(request, productId):
    product = Products.objects.get(id=productId)
    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductsForm(instance=product)

    context = { 'form' : form }
    return render(request, 'lisshop/update_product.html', context)


# Sales views


def salesList(request):
    sales = Sales.objects.all()
    context = { 'sales' : sales }
    return render(request, 'lisshop/sales.html', context)