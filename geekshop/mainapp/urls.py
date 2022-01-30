from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path("", views.products, name='products'),
    path("<int:pk>/", views.category, name='category')
]
