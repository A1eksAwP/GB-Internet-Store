from django.urls import path

import cartapp.views as cartapp

app_name = 'cartapp'

urlpatterns = [
    path('', cartapp.view, name='view'),
    path('add/<int:product_id>/', cartapp.add, name='add'),
    path('remove/<int:cart_item_id>/', cartapp.remove, name='remove'),
    path('edit/<int:cart_item_id>/<int:quantity>/', cartapp.edit, name='edit'),
]   