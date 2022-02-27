from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver

def get_activation_key_exp_date():
    return now() + timedelta(hours=48)

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст', default=18)
    phone = models.CharField(verbose_name='телефон', blank=True, max_length=20)
    city = models.CharField(verbose_name='город', blank=True, max_length=20)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_activation_key_exp_date)

class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NON_BINARY = 'X'

    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (NON_BINARY, 'Небинарный'),
    )

    user = models.OneToOneField(
        ShopUser, unique=True, 
        null=False, 
        db_index = True, 
        on_delete=models.CASCADE,
        related_name='profile',
        )
    about = models.TextField(verbose_name="о себе", max_length=512, blank=True)
    gender = models.CharField(verbose_name="гендер", choices=GENDER_CHOICES, max_length=1)

@receiver(post_save, sender=ShopUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShopUserProfile.objects.create(user=instance)
    else:
        instance.profile.save()