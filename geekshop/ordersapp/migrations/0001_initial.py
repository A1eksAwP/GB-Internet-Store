# Generated by Django 3.2.11 on 2022-03-19 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0002_productcategory_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('status', models.CharField(choices=[('CREATED', 'создан'), ('IN_PROCESSING', 'в обработке'), ('AWAITING_PAYMENT', 'AWAITING_PAYMENT'), ('PAID', 'оплачен'), ('READY', 'готов'), ('CANCELED', 'отменён'), ('FINISHED', 'выполнен')], max_length=20, verbose_name='статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ordersapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
    ]
