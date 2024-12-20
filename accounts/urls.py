"""
URL configuration for projectDocker project.

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
from django.contrib import admin
from django.urls import re_path, path
from .views import otp_login, home

#temporal

from django_otp.admin import OTPAdminSite

class OTPAdmin(OTPAdminSite):
    pass

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

admin_site = OTPAdmin()
admin_site.register(User)
admin_site.register(TOTPDevice)

urlpatterns = [
    #re_path('r^', ),
    path('', home, name='home'),
    path('login/', otp_login, name='otp_login'),
    #re_path(r'^admin/', admin_site.urls),
    #re_path(r'^dadmin/', admin.site.urls),
]
