# Generated by Django 4.2 on 2024-06-07 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0004_alter_product_views_counter_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
    ]
