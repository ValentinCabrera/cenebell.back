# Generated by Django 4.2.16 on 2024-11-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movimiento",
            name="mantenimiento",
        ),
        migrations.RemoveField(
            model_name="movimiento",
            name="tipo",
        ),
        migrations.AddField(
            model_name="material",
            name="stock_actual",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="DetalleMovimiento",
        ),
        migrations.DeleteModel(
            name="Movimiento",
        ),
        migrations.DeleteModel(
            name="TipoMovimiento",
        ),
    ]
