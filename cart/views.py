from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from stores.models import Product



def cart(request):
    cart = request.session.get('cart',{})
    products = []
    total_price = 0

    for product_id , quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            products.append({
                'product': product,
                'quantity': quantity,
                'total': product.price * quantity
            })
            total_price += product.price * quantity

        except Product.DoesNotExist:
            del cart[product_id]
            request.session['cart'] = cart

    context = {
        "cart_items" : products,
        "total_price" : total_price,
        "total_items" : sum(cart.values())

    }
    return render(request,'cart/cart.html',context)

def remove_from_cart(request,product_id):
    cart = request.session.get('cart',{})
    product_key = str(product_id)
    if cart[product_key] > 1:
        cart[product_key] -= 1
    else:
        del cart[product_key]
    request.session['cart'] = cart


    return redirect('cart')