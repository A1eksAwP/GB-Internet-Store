from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.http import HttpResponseRedirect
from django.urls import reverse
from adminapp.forms import ShopUserAdminForm, ProductCategoryAdminForm
from adminapp.utils import superuser_required


#ПОЛЬЗОВАТЕЛИ
@superuser_required
def users(request):
    title = 'Админка/Пользователи'
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content = {
        'title': title,
        'objects': users_list
    }
    return render(request, 'adminapp/user/users.html', content)

#на момент лекции не учитывалось, что нового пользователя не создать, так как нет поля для пароля
@superuser_required
def user_create(request):
    title = 'Пользователи/Создание'
    if request.method == 'POST':
        form = ShopUserAdminForm(request.POST, request.FILES)   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        form = ShopUserAdminForm()
    content = {'title': title, 'update_form': form}
    return render(request, 'adminapp/user/edit.html', content)


@superuser_required
def user_update(request, pk):
    title = 'Пользователи/Редактирование'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = ShopUserAdminForm(request.POST, request.FILES, instance=edit_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        form = ShopUserAdminForm(instance=edit_user)
    content = {'title': title, 'update_form': form}
    return render(request, 'adminapp/user/edit.html', content)


@superuser_required
def user_delete(request, pk):
    title = 'Пользователи/Удаление'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))
    content = {'title': title, 'user_to_delete': user}
    return render(request, 'adminapp/user/delete.html', content)



#КАТЕГОРИИ ПРОДУКТОВ
@superuser_required
def categories(request):
    title = 'Админка/Категории'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/category/categories.html', content)


@superuser_required
def category_create(request):
    title = 'Категории/Создание'
    if request.method == 'POST':
        form = ProductCategoryAdminForm(request.POST, request.FILES)   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategoryAdminForm()
    content = {'title': title, 'update_form': form}
    return render(request, 'adminapp/category/edit.html', content)


@superuser_required
def category_update(request, pk):
    title = 'Категории/Редактирование'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryAdminForm(request.POST, request.FILES, instance=category)   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategoryAdminForm(instance=category)
    content = {'title': title, 'update_form': form}
    return render(request, 'adminapp/category/edit.html', content)


@superuser_required
def category_delete(request, pk):
    title = 'Категории/Удаление'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return HttpResponseRedirect(reverse('admin:categories'))
    content = {'title': title, 'category_to_delete': category}
    return render(request, 'adminapp/category/delete.html', content)



#ПРОДУКТЫ
def products(request, pk):
    title = 'админка/продукт'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category=category).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/product/products.html', content)


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass