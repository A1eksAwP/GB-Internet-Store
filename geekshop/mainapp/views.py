import json
from django.shortcuts import get_object_or_404, render
from cartapp.models import Cart
from .models import ProductCategory, Product
from django.contrib.auth.decorators import login_required

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
    
@login_required
def get_product(request, store_id):
    title = 'Страница продукта'
    products = Product.objects.all()
    cart = Cart.objects.filter(user=request.user)
    item = get_object_or_404(Product, pk=store_id)
    content = {
        'title': title,
        'category': category,
        'products': products,
        'cart': cart,
        'item': item,
    }

    return render(request, 'mainapp/product_about.html', content)

@login_required
def products(request, pk=0):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    cart = Cart.objects.filter(user=request.user)
    
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

def base(request):
    return render(request, 'mainapp/base.html', context= {
        'title':'!секретная страница!'
    })