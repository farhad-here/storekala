from django.urls import path,include
from .views import *
from .views import SellerPanelView, CreateStoreView

urlpatterns = [
    path("",stores_list,name='stores_list'),
    path("<int:pk>/",store_detail, name='store_detail'),
    path('add-to-cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('add_products/<int:store_id>/',add_product, name="add_product"),
    path('seller/', SellerPanelView.as_view(), name='seller_panel'),
    path('seller/create/', CreateStoreView.as_view(), name='create_store'),
    path('seller/manage/<int:pk>/', manage_store, name='manage_store'),
    path('seller/product/<int:product_id>/edit/', edit_product, name='edit_product'),
]
