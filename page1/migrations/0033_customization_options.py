# Generated by Django 4.2.5 on 2024-03-07 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0032_tablereservation_cancel_tablereservation_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('type', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('menu_item_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page1.menutbl')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('customization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page1.customization')),
            ],
        ),
    ]
