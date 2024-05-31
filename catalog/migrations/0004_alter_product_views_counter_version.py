# Generated by Django 5.0.4 on 2024-05-31 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_product_is_published_product_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="views_counter",
            field=models.PositiveIntegerField(
                default=0,
                help_text="укажите количество просмотров",
                verbose_name="количество просмотров",
            ),
        ),
        migrations.CreateModel(
            name="Version",
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
                    "number",
                    models.PositiveIntegerField(
                        help_text="Введите номер версии", verbose_name="Номер версии"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название версии",
                        max_length=50,
                        verbose_name="Название версии",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False,
                        help_text="Отметьте активность версии",
                        verbose_name="Активная версия?",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=100, unique=True, verbose_name="slug"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        help_text="введите версию продукта",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="version",
                        to="catalog.product",
                        verbose_name="продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]