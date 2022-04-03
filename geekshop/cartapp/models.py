from django.db import models
from django.conf import settings
from numpy import delete
from mainapp.models import Product

class CartQuerySet(models.query.QuerySet):
    def delete(self, *args, **kwargs):
        for item in self:
            item.product.quantity += item.quantity
            item.product.save()
        super().delete(*args, **kwargs)

class CartManager(models.Manager):
    def count(self):
        return len(self.all())
    
    def sum(self):
        cart_sum = 0
        for item in self.all():
            cart_sum += item.product.price * item.quantity
        return cart_sum  

class Cart(models.Model):
    class Meta:
        unique_together = ['user','product']
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    objects = CartManager()

    def save(self, *args, **kwargs):
        if self.pk:
            old_cart = Cart.objects.get(pk=self.pk)
            self.product.quantity -= self.quantity - old_cart.quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        
        self.product.quantity += self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    @property
    def cost(self):
        return self.product.price*self.quantity

    def __str__(self):
        return f'{self.product.name} - {self.quantity}шт'