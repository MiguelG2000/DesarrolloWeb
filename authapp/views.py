from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
#from django.views.decorators.csrf import csrf_exempt
#from django.utils.decorators import method_decorator

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

    '''# Desactivar la protección CSRF para esta vista
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)'''

class MyTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)

    # Desactivar la protección CSRF para esta vista
    '''@method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)'''
