# Generated by Django 4.2.5 on 2023-11-22 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0015_cart_t_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page1.cart'),
        ),
    ]
