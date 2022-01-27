from email.charset import Charset
import json
from django.shortcuts import render

# Create your views here.

def main(request):
    with open ('./products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    return render(request, 'mainapp/index.html', context = {
        'title':'Главная',
        'products': products
    })

    

def products(request):
    return render(request, 'mainapp/products.html')
    

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
    menu = [
            {'name':'Шаурма1'},
            {'name':'Шаурма2'},
            {'name':'Шаурма3'},
            {'name':'Шаурма4'},
            {'name':'Шаурма5'},
            {'name':'Шаурма6'},
            {'name':'Шаурма7'},
            {'name':'Шаурма8'},
            {'name':'Шаурма9'},
        ]
    return render(request, 'mainapp/base.html', context= {
        'menu': menu,
        'title':'!секретная страница!'
    })