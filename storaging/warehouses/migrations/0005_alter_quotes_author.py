# Generated by Django 4.2.7 on 2024-03-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("warehouses", "0004_quotes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quotes",
            name="author",
            field=models.CharField(db_index=True, max_length=150, verbose_name="Автор"),
        ),
    ]
