# Generated by Django 4.1.7 on 2023-05-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("revoke_app", "0005_dish_foodcategory_dish_foodquantity_dish_foodunit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="quantity",
            field=models.FloatField(),
        ),
    ]