from lib2to3.fixes.fix_input import context
from tempfile import template

from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def first_view(request):
    return HttpResponse("<h1>Hola</h1>")

def second_view(request):
    name = "Miguel Gonzalez"
    age = 23
    age_list = [23,5,24,21,22]
    contexto = {
        "name": name,
        "age": age,
        "listas": age_list
    }
    print(r">>>>(request.method)")
    return render(
        request,
        "index.html",
        context=contexto
    )
def base_view(request):
    return render(
        request,
        "base.html"
    )

def list_build(request):
    return render(
        request,
        "product/list.html"
    )