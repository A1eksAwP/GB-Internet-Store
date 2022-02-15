from email.charset import Charset
import json
from django.shortcuts import get_object_or_404, render
from cartapp.models import Cart
from .models import ProductCategory, Product

# Create your views here.

def main(request):
    with open ('./products.json', 'r', encoding='utf-8') as file:
        jsonproducts = json.load(file)

    products = Product.objects.all()
    categorys = ProductCategory.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    else:
        cart = ""

    return render(request, 'mainapp/index.html', context = {
        'title':'Главная',
        'products': jsonproducts,
        'foods': products,
        'categorys': categorys,
        'cart': cart,
    })

def products(request, pk=0):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    else:
        cart = ""

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'cart': cart,
        }

        return render(request, 'mainapp/products_list.html', content)


def category(request, pk):
    return products(request)

def contact(request):
    return render(request, 'mainapp/contact.html', context = {
        'title':'Контакты',
    })

def about(request):
    return render(request, 'mainapp/about.html', context = {
        'title':'О нас',
    })

def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    else:
        cart = ""
    return render(request, 'mainapp/cart.html', context = {
        'title':'Корзина',
        'cart': cart,
    })

def base(request):
    return render(request, 'mainapp/base.html', context= {
        'title':'!секретная страница!'
    })