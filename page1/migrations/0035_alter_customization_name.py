# Generated by Django 4.2.5 on 2024-04-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0034_alter_customization_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customization',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]