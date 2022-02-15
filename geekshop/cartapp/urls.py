from django.urls import path

import cartapp.views as usercartapp

app_name = 'cartapp'

urlpatterns = [
    path('', usercartapp.view, name='view'),
    path('add/<int:product_id>', usercartapp.add, name='add'),
    path('remove/<int:cart_item_id>', usercartapp.remove, name='remove'),
    path('plus/<int:product_id>', usercartapp.plus, name='plus'),
    path('minus/<int:product_id>', usercartapp.minus, name='minus'),
]   