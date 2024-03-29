# Generated by Django 4.1.7 on 2023-05-28 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("revoke_app", "0004_foodcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="foodCategory",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="revoke_app.foodcategory",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="dish",
            name="foodQuantity",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="dish",
            name="foodUnit",
            field=models.PositiveIntegerField(
                blank=True,
                choices=[(1, "Kilogram"), (2, "Pound"), (3, "Litter"), (4, "")],
                default=1,
                null=True,
            ),
        ),
    ]
