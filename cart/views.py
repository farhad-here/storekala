# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stores.models import Product, Order, OrderItem
from accounts.models import Profile

def cart(request):
    cart = request.session.get('cart', {})
    products = []
    total_price = 0
    for product_id, quantity in cart.items():
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
        'cart_items': products,
        'total_price': total_price,
        'total_items': sum(cart.values())
    }
    return render(request, 'cart/cart.html', context)


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_key = str(product_id)
    if cart[product_key] > 1:
        cart[product_key] -= 1
    else:
        del cart[product_key]
    request.session['cart'] = cart
    return redirect('cart')


@login_required
def checkout(request):
    cart_data = request.session.get('cart', {})

    if not cart_data:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart')

    items = []
    total_price = 0
    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, id=int(product_id))
        subtotal = product.price * quantity
        total_price += subtotal
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if profile.balance < total_price:
            messages.error(request, f'موجودی کافی نیست. موجودی شما: {profile.balance} تومان')
            return redirect('checkout')

        for item in items:
            if item['product'].stock < item['quantity']:
                messages.error(request, f"موجودی {item['product'].name} کافی نیست.")
                return redirect('cart')

        order = Order.objects.create(
            user=request.user,
            total=total_price,
            status='paid'
        )

        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price,
            )
            item['product'].stock -= item['quantity']
            item['product'].save()

        profile.balance -= total_price
        profile.save()

        request.session['cart'] = {}

        messages.success(request, f'سفارش #{order.id} با موفقیت ثبت شد!')
        return redirect('order_history')

    return render(request, 'cart/checkout.html', {
        'items': items,
        'total_price': total_price,
        'balance': profile.balance,
    })


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    return render(request, 'cart/order_history.html', {'orders': orders})