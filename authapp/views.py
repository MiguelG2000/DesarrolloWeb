from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'This is a protected endpoint in the client service.'}
        return Response(content)

