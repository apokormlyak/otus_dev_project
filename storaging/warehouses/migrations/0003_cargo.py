# Generated by Django 4.2.7 on 2024-03-14 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("warehouses", "0002_storagetype"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cargo",
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
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=64, verbose_name="Наименование груза"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Описание"
                    ),
                ),
                ("cargo_value", models.FloatField(verbose_name="Объем груза")),
                ("cargo_weight", models.FloatField(verbose_name="Вес груза")),
                (
                    "storage_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.storagetype",
                        verbose_name="Тип хранения",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouses.warehouse",
                        verbose_name="Склад",
                    ),
                ),
            ],
            options={
                "verbose_name": "Груз",
                "verbose_name_plural": "Грузы",
            },
        ),
    ]
