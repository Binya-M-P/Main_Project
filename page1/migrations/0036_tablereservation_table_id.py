# Generated by Django 4.2.5 on 2024-04-14 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page1', '0035_alter_customization_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablereservation',
            name='table_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations_as_table', to=settings.AUTH_USER_MODEL),
        ),
    ]
