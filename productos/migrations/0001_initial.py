# Generated by Django 4.2.4 on 2023-09-01 13:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
import productos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('remisiones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', productos.models.UpperField(max_length=10, unique=True)),
                ('nombre', productos.models.LowerField(max_length=150)),
                ('marca', productos.models.LowerField(blank=True, max_length=150, null=True)),
                ('cantidad', models.IntegerField()),
                ('peso', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recepcion', models.DateField(default=datetime.date(2023, 9, 1))),
                ('orden', models.BooleanField(default=False)),
                ('usuario', productos.models.LowerField(default='', max_length=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('proveedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='RemiProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('peso', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('remision_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remisiones.remisiones')),
            ],
        ),
        migrations.CreateModel(
            name='ReceProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('recepcion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.recepcion')),
            ],
        ),
    ]
