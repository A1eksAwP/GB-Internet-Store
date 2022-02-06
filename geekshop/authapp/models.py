from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')
    phone = models.CharField(verbose_name='телефон', max_length=20)
    city = models.CharField(verbose_name='город', max_length=20)