from django.urls import path
import mainapp.views as mainapp
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('product/<int:store_id>/', mainapp.get_product, name='product'),

]
