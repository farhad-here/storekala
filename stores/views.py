from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib import messages
from .forms import *

def stores_list(request):
    stores = Store.objects.select_related('owner')
    return render(request, 'stores/stores.html',{'stores':stores})



def store_detail(request,pk):
    store = get_object_or_404(Store, pk=pk)
    products = store.products.filter(is_active=True , stock__gt=0)
    return render(request, 'stores/store_detail.html',{'products':products, 'store':store})
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    cart = request.session.get('cart',{})
    product_key = str(product_id)

    if product_key in cart:
        if product.stock > cart[product_key]:
            cart[product_key]+= 1
        else:
            messages.error(request,"Not enough stock")

    else:
        cart[product_key]= 1

    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'home:index'))


def add_product(request,store_id):
    store = get_object_or_404(Store, id=store_id)
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES)
        if form.is_valid:
            product = form.save(commit=False)
            product.store = store
            product.save()
            return redirect('store_detail', pk=store.id)
        else:
            messages.error(request, 'لطفاً خطاهای فرم را اصلاح کنید.')
    else:
        # ۶. نمایش فرم خالی
        form = AddProductForm()

    context = {
        'store': store,
        'form': form,
    }
    return render(request, 'add_product.html', context)
