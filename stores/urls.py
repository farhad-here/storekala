from django.urls import path,include
from .views import *

urlpatterns = [
    path("stores/",stores_list,name='stores_list'),
    path("stores/<int:pk>/",store_detail, name='store_detail')
]
