# Generated by Django 4.2.16 on 2025-01-18 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("maquinas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fabricante",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TipoMaquina",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                (
                    "fabricante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="maquinas.fabricante",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="maquina",
            name="tipo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="maquinas.tipomaquina",
            ),
        ),
    ]
