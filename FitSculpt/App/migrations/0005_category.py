# Generated by Django 4.2.15 on 2025-01-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_product_alter_client_options_alter_clientfm_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
