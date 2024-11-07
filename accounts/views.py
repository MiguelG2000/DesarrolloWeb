from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.cache import cache
from django_otp.plugins.otp_totp.models import TOTPDevice

from users.models import Post
from .forms import OTPLoginForm

def otp_login(request):
    if request.method == 'POST':
        form = OTPLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            otp_token = form.cleaned_data['otp_token']

            # Autenticación del usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Verificar el token OTP
                try:
                    device = TOTPDevice.objects.get(user=user, confirmed=True)
                    if device.verify_token(otp_token):
                        # Login exitoso, redirige a la página de inicio
                        login(request, user)

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

                        return render(request, 'base.html',context)
                    else:
                        messages.error(request, "OTP token inválido.")
                except TOTPDevice.DoesNotExist:
                    messages.error(request, "No se encontró dispositivo OTP para este usuario.")
            else:
                messages.error(request, "Credenciales inválidas.")
    else:
        form = OTPLoginForm()

    return render(request, 'accounts/otp_login.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')
