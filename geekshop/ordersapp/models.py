from django.dispatch import receiver
from mainapp.models import Product
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete, pre_save

# Create your models here.
class Order(models.Model):

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    CREATED = 'CREATED'
    IN_PROCESSING = 'IN_PROCESSING'
    AWAITING_PAYMENT = 'AWAITING_PAYMENT'
    PAID = 'PAID'
    READY = 'READY'
    CANCELED = 'CANCELED'
    FINISHED = 'FINISHED'

    ORDER_STATUS_CHOICES = (
        (CREATED,'создан'),
        (IN_PROCESSING, 'в обработке'),
        (AWAITING_PAYMENT, 'ожидает оплаты'),
        (PAID, 'оплачен'),
        (READY,'готов'),
        (CANCELED, 'отменён'),
        (FINISHED, 'выполнен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="обновлен", auto_now=True)
    status = models.CharField(verbose_name="статус", choices=ORDER_STATUS_CHOICES, max_length=30, default=CREATED)
    is_active = models.BooleanField(verbose_name="активен", default=True)

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.select_related('product'))

    def get_total_cost(self):
        return sum(item.cost for item in self.items.select_related('product'))

    def __str__(self):
        return f'Заказ {self.id}'

        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    @property
    def cost(self):
        return self.product.price * self.quantity

@receiver(pre_save, sender=OrderItem)
def product_quantity_upd_on_order_item_save(
    sender, update_fields, instance, **kwargs
):
    if instance.pk:
        old_item = OrderItem.objects.get(pk=instance.pk)
        instance.product.quantity -= instance.quantity - old_item.quantity
    else:
        instance.product.quantity -= instance.quantity
    instance.product.save()

@receiver(pre_delete, sender=OrderItem)
def product_quantity_upd_on_order_item_delete( sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()