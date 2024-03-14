# Generated by Django 4.2.7 on 2024-03-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Warehouse",
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
                        db_index=True, max_length=64, verbose_name="Наименование склада"
                    ),
                ),
                ("address", models.CharField(max_length=150, verbose_name="Адрес")),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Описание"
                    ),
                ),
                ("useful_value", models.FloatField(verbose_name="Площадь")),
            ],
            options={
                "verbose_name": "Склад",
                "verbose_name_plural": "Склады",
            },
        ),
    ]
