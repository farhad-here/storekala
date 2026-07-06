from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Store
from .forms import StoreForm
from django.core.exceptions import PermissionDenied

# store
def stores_list(request):
    stores = Store.objects.select_related('owner').filter(is_active=True)
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
            messages.success(request, 'Added to cart successfully.')

        else:
            messages.error(request,message="Not enough stock")

    else:
        cart[product_key]= 1
        messages.success(request, 'Added to cart successfully.')

    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', '/'))

# product
def add_product(request,store_id):
    store = get_object_or_404(Store, id=store_id)
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            return redirect('store_detail', pk=store.id)
        else:
            messages.error(request, 'لطفاً خطاهای فرم را اصلاح کنید.')
    else:
        
        form = AddProductForm()

    context = {
        'store': store,
        'form': form,
    }
    return render(request, 'add_product.html', context)

# seller_panel
@method_decorator(login_required, name='dispatch')
class SellerPanelView(ListView):
    model = Store
    template_name = 'stores/seller_panel.html'
    context_object_name = 'stores'

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user).order_by('-created_at')


@method_decorator(login_required, name='dispatch')
class CreateStoreView(CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'stores/create_store.html'
    success_url = reverse_lazy('seller_panel')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        self.request.user.is_seller = True
        self.request.user.save()
        return response
    

@login_required
def manage_store(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if store.owner != request.user:
        raise PermissionDenied
    
    products = store.products.all()
    store_form = StoreForm(instance=store)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'update_store':
            store_form = StoreForm(request.POST, instance=store)
            if store_form.is_valid():
                store_form.save()
                messages.success(request, 'Store updated successfully.')
                return redirect('manage_store', pk=pk)
        
        elif action == 'delete_product':
            product_id = request.POST.get('product_id')
            product = get_object_or_404(Product, id=product_id, store=store)
            product.delete()
            messages.success(request, 'Product deleted.')
            return redirect('manage_store', pk=pk)

        elif action == 'update_stock':  # ← اضافه کن
            product_id = request.POST.get('product_id')
            new_stock = request.POST.get('stock')
            try:
                new_stock = int(new_stock)

                # حداکثر مقدار قابل قبول
                if new_stock < 0:
                    raise ValueError("Stock cannot be negative.")

                if new_stock > 1000000:   # یا هر مقداری که برای پروژه مناسب است
                    raise ValueError("Stock is too large.")
                product = get_object_or_404(Product, id=product_id, store=store)
                product.stock = new_stock
                product.save()
                messages.success(request, f'Stock updated for {product.name}.')
            except ValueError as e:
                messages.error(request, str(e))
            return redirect('manage_store', pk=pk)
    
    return render(request, 'stores/manage_store.html', {
        'store': store,
        'products': products,
        'store_form': store_form,
    })


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if product.store.owner != request.user:
        raise PermissionDenied
    
    form = AddProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product updated.')
        return redirect('manage_store', pk=product.store.pk)
    
    return render(request, 'stores/edit_product.html', {
        'form': form,
        'product': product,
    })