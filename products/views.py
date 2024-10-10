
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from products.models import Product
from products.forms import ProductForm
from django.views.generic import (
    ListView,
    View
)
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def products_list_view(request):
    products = []
    # if 'Editor' in request.user.groups.values_list(
    #     'name',
    #     flat=True
    # ):
    if request.user.is_superuser:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(
                user=request.user,
                # is_active=True,
        )
    context = {
        "products": products
    }
    return render(request, "product/list.html", context=context)

def product_create_view(request):
    if request.method == "POST":
        product = Product()
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.user = request.user
        product.save()
        return redirect(reverse_lazy("list-products-view"))
    return render(
        request,
        "product/form.html",
    )

def product_update_view(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.user = request.user
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


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()


class ProductView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        data = {
            "mensaje": "Esto es una respuesta GET en JSON",
            "método": "GET",
            "status": "success"
        }
        return JsonResponse(data)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
