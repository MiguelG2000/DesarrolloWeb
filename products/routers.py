from rest_framework import routers
from products.viewsets import ProdcutsViewsets

router = routers.DefaultRouter()

router.register(
    'products',
    ProdcutsViewsets
)