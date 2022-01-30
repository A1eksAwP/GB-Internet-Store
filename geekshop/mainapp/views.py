from email.charset import Charset
import json
from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.

def main(request):
    with open ('./products.json', 'r', encoding='utf-8') as file:
        jsonproducts = json.load(file)

    products = Product.objects.all()
    categorys = ProductCategory.objects.all()

    return render(request, 'mainapp/index.html', context = {
        'title':'Главная',
        'products': jsonproducts,
        'foods': products,
        'categorys': categorys
    })

def products(request):
    return render(request, 'mainapp/index.html')

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
    return render(request, 'mainapp/cart.html', context = {
        'title':'Корзина',
    })

def base(request):
    return render(request, 'mainapp/base.html', context= {
        'title':'!секретная страница!'
    })