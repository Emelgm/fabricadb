# Generated by Django 4.2.4 on 2023-08-28 21:16

from django.db import migrations
import remisiones.models


class Migration(migrations.Migration):

    dependencies = [
        ('remisiones', '0002_alter_remisiones_codigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remisiones',
            name='codigo',
            field=remisiones.models.UpperField(max_length=10, unique=True),
        ),
    ]