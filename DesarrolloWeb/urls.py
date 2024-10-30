"""
URL configuration for proyecto2024B project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from users.views import (
    first_view,
    second_view,
    base_view,
    list_build,
)

schema_view = get_schema_view(
    openapi.Info(
        title="API de Biblioteca",
        default_version='v1',
        description="API para gestionar libros",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@biblioteca.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #path('', include('authapp.urls')),
    path('admin/', admin.site.urls),
    path('users/', first_view, name="first-view"),
    path('users2/', second_view, name="second-view"),
    path('products/', include("products.urls")),
    path('', LoginView.as_view(template_name="base.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)