from django.urls import path
from products.views import (
    products_list_view,
    product_create_view,
    product_update_view,
    product_delete_view
)
urlpatterns = [
    path('list/', products_list_view, name="list-products-view"),
    path('create/', product_create_view, name="create-products-view"),
    path('update/<int:product_id>/', product_update_view, name="update-products-view"),
    path('delete/<int:product_id>/', product_delete_view, name="delete-products-view"),

]