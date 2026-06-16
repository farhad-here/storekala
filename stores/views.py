from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *




def stores_list(request):
    stores = Store.objects.select_related('owner')
    return render(request, 'stores/stores.html',{'stores':stores})



def store_detail(request,pk):
    store = get_object_or_404(Store, pk=pk)
    products = store.products.filter(is_active=True , stock__gt=0)
    return render(request, 'stores/store_detail.html',{'products':products})
