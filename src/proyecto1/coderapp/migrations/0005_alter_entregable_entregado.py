# Generated by Django 5.0 on 2023-12-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderapp', '0004_rename_entrega_entregable_entregado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='entregado',
            field=models.BooleanField(),
        ),
    ]