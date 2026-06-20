from django.urls import path
from .views import cart, remove_from_cart, checkout, order_history

urlpatterns = [
    path('', cart, name='cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', order_history, name='order_history'),
]