from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from products.models import Product
from products.forms import ProductForm

# Create your views here.
def products_list_view(request):
    #products = [] if 'editor' in request.user.groups.values_list('name',flat=True):
    if request.user.is_superuser:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(
            user=request.user,
            is_active=True
            )
    context = {
        'products':products
    }
    return render(
        request, "product/list.html",
        context=context
    )

def product_create_view(request):
    if request.method == 'POST':
        products = Product()
        products.name = request.POST['name']
        products.description = request.POST['description']
        products.price = request.POST['price']
        products.user = request.user
        products.save()
        return redirect(reverse_lazy("list-products-view"))
    return render(
        request, "product/form.html",
    )

def product_update_view(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect(reverse_lazy("list-products-view"))
    context = {
        "product": product
    }
    return render(
        request,
        "product/form.html",
        context=context
    )
def product_delete_view(request, product_id):
    Product.objects.get(id=product_id).delete()
    return redirect(reverse_lazy("list-products-view"))

