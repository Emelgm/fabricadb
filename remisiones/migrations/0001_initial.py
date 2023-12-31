# Generated by Django 4.2.4 on 2023-09-22 13:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
import remisiones.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remisiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', remisiones.models.UpperField(max_length=10, unique=True)),
                ('fecha_despacho', models.DateField(default=datetime.date(2023, 9, 22))),
                ('estado', models.BooleanField(default=True)),
                ('orden', models.BooleanField(default=False)),
                ('usuario', remisiones.models.LowerField(default='', max_length=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]
