from django.urls import path,include
from .views import *

urlpatterns = [
    path("",stores_list,name='stores_list'),
    path("<int:pk>/",store_detail, name='store_detail'),
    path('add-to-cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('add_products/<int:store_id>/',add_product, name="add_product")
]
