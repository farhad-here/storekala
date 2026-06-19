from django.shortcuts import render
from stores.models import Product
from django.views.generic import ListView

class HomePageView(ListView):
    model = Product
    template_name = 'home/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('store').order_by('-created_at')