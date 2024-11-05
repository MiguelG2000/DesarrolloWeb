from django.http import HttpResponse
from .models import Post
from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth.views import LoginView


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

def login(request):
    if not request.user.is_authenticated:
        return LoginView.as_view(template_name="base.html")(request)

    # Si está autenticado, recuperar la información para el dashboard
    posts = Post.objects.all()
    user = request.user
    full_name = user.get_full_name()
    groups = user.groups.all()

    ct = cache.get('count', version=user.pk)
    context = {
        'posts': posts,
        'full_name': full_name,
        'groups': groups,
        'ct': ct
    }

    return render(request, 'base.html', context)
