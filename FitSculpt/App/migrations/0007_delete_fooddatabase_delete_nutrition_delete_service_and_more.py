# Generated by Django 4.2.15 on 2024-09-21 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_fooddatabase_nutrition_payment_service_workout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoodDatabase',
        ),
        migrations.DeleteModel(
            name='Nutrition',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
