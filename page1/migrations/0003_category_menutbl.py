# Generated by Django 4.2.5 on 2023-10-03 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Menutbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page1.category')),
            ],
        ),
    ]
