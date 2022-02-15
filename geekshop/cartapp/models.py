from django.db import models
from django.conf import settings
from mainapp.models import Product

class CartManager(models.Manager):
    def count(self):
        return len(self.all())
    
    def sum(self):
        cart_sum = 0
        for item in self.all():
            cart_sum += item.product.price * item.quantity
        return cart_sum

    # def minus(self):
    #     for item in self:
    #         if item.quantity>1:
    #             item.quantity-=1
    #         else:
    #             item.quantity=1
    #     return item.quantity

    # def plus(self):
    #     for item in self:
    #         if item.quantity>1:
    #             item.quantity+=1
    #         else:
    #             item.quantity=1
    #     return item.quantity    

class Cart(models.Model):
    class Meta:
        unique_together = ['user','product']
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usercart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
    objects = CartManager()

    def __str__(self):
        return f'{self.product.name} - {self.quantity}шт'