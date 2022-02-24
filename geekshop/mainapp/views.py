import json
from turtle import title
from django.shortcuts import get_object_or_404, render
from .models import ProductCategory, Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def main(request):
    with open ('./products.json', 'r', encoding='utf-8') as file:
        jsonproducts = json.load(file)

    title = 'главная'
    products = Product.objects.all()
    categorys = ProductCategory.objects.all()

    return render(request, 'mainapp/index.html', context = {
        'title': title,
        'products': jsonproducts,
        'foods': products,
        'categorys': categorys,
    })
    
@login_required
def get_product(request, store_id):
    title = 'Страница продукта'
    products = Product.objects.all()
    item = get_object_or_404(Product, pk=store_id)
    content = {
        'title': title,
        'category': category,
        'products': products,
        'item': item,
    }

    return render(request, 'mainapp/product_about.html', content)

@login_required
def products(request, pk=0, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(category__is_active=True).order_by('price')
            category = {
                'pk': 0,
                'name': 'все',
                }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'page': products_paginator,
            'paginator': paginator,
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

def base(request):
    return render(request, 'mainapp/base.html', context= {
        'title':'!секретная страница!'
    })