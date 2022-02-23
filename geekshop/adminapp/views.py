from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.http import HttpResponseRedirect
from django.urls import reverse
from adminapp.forms import ShopUserAdminForm, ProductCategoryAdminForm, ProductEditAdminForm
from adminapp.utils import superuser_required
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


#ПОЛЬЗОВАТЕЛИ
class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/user/users.html'
    paginate_by = 1
    
    @method_decorator(superuser_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user/edit.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserAdminForm

    @method_decorator(superuser_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user/edit.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserAdminForm

    @method_decorator(superuser_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи/Редактирование'
        
        return context 

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user/delete.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(superuser_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url()) 


#КАТЕГОРИИ ПРОДУКТОВ
class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/category/categories.html'

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category/edit.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'
    
class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category/edit.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории/Редактирование'
    
        return context 

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category/delete.html'
    success_url = reverse_lazy('admin:categories')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url()) 


#ПРОДУКТЫ
class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product/products.html'

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        context['category'] = self.get_category()

        return context 

class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/product/products.html' 

class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product/edit.html'
    success_url = reverse_lazy('admin:products')
    fields = '__all__'

    def get_initial(self):
        return {
            'category': self.get_category()
        }

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category()
    
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product/edit.html'
    success_url = reverse_lazy('admin:products')
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукт/Редактирование'
        
        return context 

class ProductDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/product/delete.html'
    success_url = reverse_lazy('admin:products')

    @method_decorator(superuser_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url()) 