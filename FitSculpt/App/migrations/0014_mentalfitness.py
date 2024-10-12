# Generated by Django 4.2.15 on 2024-10-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentalFitness',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.IntegerField()),
                ('fm_id', models.IntegerField()),
                ('client_name', models.CharField(max_length=50)),
                ('fm_name', models.CharField(max_length=50)),
                ('current_mood', models.CharField(max_length=1000)),
                ('distribution', models.CharField(max_length=1000)),
                ('session_link', models.CharField(max_length=500)),
                ('timing', models.CharField(max_length=50)),
                ('class_time', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_mental_fitness',
                'managed': False,
            },
        ),
    ]