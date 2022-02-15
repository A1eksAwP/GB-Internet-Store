from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from cartapp.models import Cart
from mainapp.models import Product




def view(request):
    return render(request, 'cartapp/usercart.html', context = {
        'cart': Cart.objects.filter(user=request.user)
    })

#Не получилось пока сделать это. Хотел отсюда сделать изменение кол-ва товаров в корзине
def plus(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.quantity += 1
    product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def minus(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(user=request.user, product=product)
    if cart.product.quantity>1:
        cart.product.quantity-=1
    else:
        cart.product.quantity=1
        
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    cart_items = Cart.objects.filter(user=request.user, product=product)

    if cart_items:
        cart = cart_items.first()
    else:
        cart = Cart(user=request.user, product=product)

    cart.quantity += 1
    cart.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
def remove(request, cart_item_id):
    cart = get_object_or_404( Cart, pk=cart_item_id )
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))