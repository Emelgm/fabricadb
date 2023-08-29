# Generated by Django 4.2.4 on 2023-08-27 20:51

import clientes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', clientes.models.UpperField(blank=True, max_length=10, null=True, unique=True)),
                ('nombre', clientes.models.LowerField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', clientes.models.LowerField(blank=True, max_length=150, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', clientes.models.LowerField(blank=True, max_length=50, null=True)),
                ('email', clientes.models.LowerField(blank=True, max_length=100, null=True)),
                ('direccion', clientes.models.LowerField(blank=True, max_length=150, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
