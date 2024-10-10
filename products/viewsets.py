from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import JsonResponse
from products.models import Product
from products.serializer import (
    ProductSerializer,
    LoginSerializer
)



class ProdcutsViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class LoginViewsets(APIView):
#
#     def post(self, request):
#         print(request)
#         return JsonResponse(
#             {
#                 "status": "Login"
#             }
#         )