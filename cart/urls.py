from django.urls import path,include
from .views import *



urlpatterns = [
    path('',cart,name='cart'),
    path('<int:product_id>/',remove_from_cart,name='remove_from_cart')

]